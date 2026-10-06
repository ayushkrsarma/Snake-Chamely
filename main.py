import pygame
import random

from entities.snake import Snake
from entities.chicken import Chicken
from entities.cactus import Cactus
from entities.ruby import Ruby
from entities.banana import Banana

from screens.start_screen import StartScreen
from screens.help import Help
from screens.about import About

from game.events import handle_events
from game.update import update_game
from game.draw import draw_game


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    snake = Snake()

    chickens = [
        Chicken(SCREEN_WIDTH, SCREEN_HEIGHT)
        for _ in range(4)
    ]

    # Only first chicken active
    for chicken in chickens:
        chicken.active = False

    chickens[0].respawn()

    cactus = Cactus(
        SCREEN_WIDTH,
        SCREEN_HEIGHT
    )

    cactus.random_position(chickens[0])
    cactus.active = True

    ruby = Ruby(
        SCREEN_WIDTH,
        SCREEN_HEIGHT
    )

    banana = Banana(
        SCREEN_WIDTH,
        SCREEN_HEIGHT
    )

    ruby.active = False
    banana.active = False

    score = 0

    timers = {
        "special": 0,
        "item_vanish": 0,
        "ruby_chicken": 0,
        "move": 0,

        "ruby_chicken_mode": False,
        "ruby_chicken_delay": 15000,

        "item_vanish_delay": 10000,

        "special_spawn_delay": 0,
        "special_index": 0,

        "special_spawn_order": [
            "banana",
            "banana",
            "banana",
            "ruby"
        ]
    }

    random.shuffle(
        timers["special_spawn_order"]
    )

    first_item = timers["special_spawn_order"][0]

    if first_item == "banana":

        timers["special_spawn_delay"] = random.randint(
            3000,
            5000
        )

    else:

        timers["special_spawn_delay"] = random.randint(
            120000,
            140000
        )

    return (
        snake,
        chickens,
        cactus,
        ruby,
        banana,
        score,
        timers
    )


# =========================================================
# PYGAME INITIALIZATION
# =========================================================

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

clock = pygame.time.Clock()


# =========================================================
# GAME OBJECTS
# =========================================================

(
    snake,
    chickens,
    cactus,
    ruby,
    banana,
    score,
    timers
) = reset_game()


# =========================================================
# SOUNDS
# =========================================================

pygame.mixer.music.load(
    "assets/sound/horrorWind.mp3"
)

pygame.mixer.music.play(-1)


eat_sound = pygame.mixer.Sound(
    "assets/sound/chicken.mp3"
)

cactus_eat = pygame.mixer.Sound(
    "assets/sound/cactus.mp3"
)

ruby_eat = pygame.mixer.Sound(
    "assets/sound/ruby.mp3"
)

banana_eat = pygame.mixer.Sound(
    "assets/sound/banana.mp3"
)


sounds = {
    "chicken": eat_sound,
    "cactus": cactus_eat,
    "ruby": ruby_eat,
    "banana": banana_eat
}


# =========================================================
# FONT
# =========================================================

font = pygame.font.Font(
    None,
    40
)


# =========================================================
# SCREENS
# =========================================================

start_screen = StartScreen(screen)

help_screen = Help(screen)

about_screen = About(screen)


# =========================================================
# GAME STATE
# =========================================================

game_state = "start"

running = True


# =========================================================
# MAIN GAME LOOP
# =========================================================

while running:

    # -----------------------------------------------------
    # TIME
    # -----------------------------------------------------

    dt = clock.tick(60)


    # -----------------------------------------------------
    # EVENTS
    # -----------------------------------------------------

    running, game_state = handle_events(
        game_state,
        running,
        snake,
        about_screen
    )


    # -----------------------------------------------------
    # UPDATE
    # -----------------------------------------------------

    if game_state == "game":

        score, game_over = update_game(
            dt,
            snake,
            chickens,
            cactus,
            ruby,
            banana,
            timers,
            sounds,
            score
        )

        # ---------------------------------------------
        # GAME OVER
        # ---------------------------------------------

        if game_over:

            game_state = "start"

            (
                snake,
                chickens,
                cactus,
                ruby,
                banana,
                score,
                timers
            ) = reset_game()


    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    if game_state == "start":

        start_screen.update(dt)
        start_screen.draw()

    elif game_state == "help":

        help_screen.draw()

    elif game_state == "about":

        about_screen.draw()

    elif game_state == "game":

        draw_game(
            screen,
            snake,
            chickens,
            cactus,
            ruby,
            banana,
            font,
            score
        )


    # -----------------------------------------------------
    # DISPLAY
    # -----------------------------------------------------

    pygame.display.flip()


# =========================================================
# QUIT
# =========================================================

pygame.quit()