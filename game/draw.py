import pygame


def draw_game(screen, snake, chickens, cactus, ruby, banana, font, score):

    screen.fill("black")

    # Snake
    for part in snake.body:

        pygame.draw.rect(
            screen,
            (57, 255, 20),
            part
        )

    # Score
    score_text = font.render(
        f"MUKTI: {score}",
        True,
        (255, 0, 255)
    )

    # Chickens
    for chicken in chickens:
        chicken.draw(screen)

    # Cactus
    cactus.draw(screen)

    # Ruby
    ruby.draw(screen)

    # Banana
    banana.draw(screen)

    # Score
    screen.blit(
        score_text,
        (20, 20)
    )