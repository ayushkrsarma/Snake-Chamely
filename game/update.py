import random


# =========================================================
# MAIN GAME UPDATE
# =========================================================

def update_game(
    dt,
    snake,
    chickens,
    cactus,
    ruby,
    banana,
    timers,
    sounds,
    score
):

    game_over = False

    # =====================================================
    # TIMERS
    # =====================================================

    timers["special"] += dt
    timers["item_vanish"] += dt

    if timers["ruby_chicken_mode"]:
        timers["ruby_chicken"] += dt

    # =====================================================
    # RUBY CHICKEN MODE
    # =====================================================

    update_ruby_chickens(
        timers,
        chickens
    )

    # =====================================================
    # SPECIAL ITEMS
    # =====================================================

    update_special_items(
        timers,
        ruby,
        banana
    )

    # =====================================================
    # SNAKE MOVEMENT
    # =====================================================

    timers["move"] += dt

    if timers["move"] >= snake.move_delay:

        snake.move()

        timers["move"] = 0

        # =================================================
        # CHICKEN COLLISION
        # =================================================

        score = check_chicken_collision(
            snake,
            chickens,
            sounds["chicken"],
            score
        )

        # =================================================
        # CACTUS COLLISION
        # =================================================

        score, cactus_game_over = check_cactus_collision(
            snake,
            chickens,
            cactus,
            sounds["cactus"],
            score
        )

        if cactus_game_over:
            game_over = True

        # =================================================
        # RUBY COLLISION
        # =================================================

        check_ruby_collision(
            snake,
            chickens,
            cactus,
            ruby,
            timers,
            sounds["ruby"]
        )

        # =================================================
        # BANANA COLLISION
        # =================================================

        check_banana_collision(
            snake,
            banana,
            timers,
            sounds["banana"]
        )

    return score, game_over


# =========================================================
# RUBY CHICKEN SYSTEM
# =========================================================

def update_ruby_chickens(
    timers,
    chickens
):

    if (
        timers["ruby_chicken_mode"]
        and timers["ruby_chicken"] >=
        timers["ruby_chicken_delay"]
    ):

        # Remove all Ruby-generated chickens
        for chicken in chickens:
            chicken.active = False

        # Bring back one normal chicken
        chickens[0].respawn()

        # Reset Ruby chicken mode
        timers["ruby_chicken"] = 0
        timers["ruby_chicken_mode"] = False


# =========================================================
# SPECIAL ITEM SYSTEM
# =========================================================

def update_special_items(
    timers,
    ruby,
    banana
):

    # =====================================================
    # SPAWN
    # =====================================================

    if (
        not ruby.active
        and not banana.active
        and timers["special"] >=
        timers["special_spawn_delay"]
    ):

        next_item = timers["special_spawn_order"][
            timers["special_index"]
        ]

        if next_item == "banana":

            banana.respawn()

        elif next_item == "ruby":

            ruby.respawn()

        # Reset item timers
        timers["special"] = 0
        timers["item_vanish"] = 0

        # Move to next item
        timers["special_index"] += 1

        prepare_next_special(timers)

    # =====================================================
    # VANISH
    # =====================================================

    if (
        (ruby.active or banana.active)
        and timers["item_vanish"] >=
        timers["item_vanish_delay"]
    ):

        ruby.active = False
        banana.active = False

        timers["item_vanish"] = 0
        timers["special"] = 0


# =========================================================
# PREPARE NEXT SPECIAL ITEM
# =========================================================

def prepare_next_special(timers):

    # =====================================================
    # COMPLETED ONE GROUP
    # 3 BANANAS + 1 RUBY
    # =====================================================

    if timers["special_index"] >= 4:

        timers["special_spawn_order"] = [
            "banana",
            "banana",
            "banana",
            "ruby"
        ]

        random.shuffle(
            timers["special_spawn_order"]
        )

        timers["special_index"] = 0

    # =====================================================
    # GET NEXT ITEM
    # =====================================================

    next_item = timers["special_spawn_order"][
        timers["special_index"]
    ]

    # =====================================================
    # NEXT SPAWN DELAY
    # =====================================================

    if next_item == "banana":

        timers["special_spawn_delay"] = random.randint(
            3000,
            5000
        )

    elif next_item == "ruby":

        timers["special_spawn_delay"] = random.randint(
            120000,
            140000
        )


# =========================================================
# CHICKEN COLLISION
# =========================================================

def check_chicken_collision(
    snake,
    chickens,
    eat_sound,
    score
):

    for chicken in chickens:

        if (
            chicken.active
            and snake.body[0].colliderect(
                chicken.rect
            )
        ):

            # Grow snake
            snake.grow()

            # Remove chicken
            chicken.eat()

            # Add chicken points
            score += chicken.points

            # Play sound
            eat_sound.play()

    # If all chickens are eaten,
    # return to one normal chicken
    if not any(
        chicken.active
        for chicken in chickens
    ):

        chickens[0].respawn()

    return score


# =========================================================
# RUBY COLLISION
# =========================================================

def check_ruby_collision(
    snake,
    chickens,
    cactus,
    ruby,
    timers,
    ruby_sound
):

    if (
        ruby.active
        and snake.body[0].colliderect(
            ruby.rect
        )
    ):

        # Ruby makes snake grow
        snake.grow()

        # Ruby gives NO points

        # Respawn all four chickens
        for chicken in chickens:
            chicken.respawn()

        # Put cactus near first chicken
        cactus.random_position(
            chickens[0]
        )

        cactus.active = True

        # Ruby disappears
        ruby.eat(chickens)

        # Play Ruby sound
        ruby_sound.play()

        # Start Ruby chicken mode
        timers["special"] = 0
        timers["item_vanish"] = 0
        timers["ruby_chicken"] = 0

        timers["ruby_chicken_mode"] = True


# =========================================================
# CACTUS COLLISION
# =========================================================

def check_cactus_collision(
    snake,
    chickens,
    cactus,
    cactus_sound,
    score
):

    game_over = False

    if (
        cactus.active
        and snake.body[0].colliderect(
            cactus.rect
        )
    ):

        # Remove cactus temporarily
        cactus.eat()

        # Play sound
        cactus_sound.play()

        # Cactus score
        score += cactus.points

        # =================================================
        # GAME OVER
        # =================================================

        if len(snake.body) == 1:

            game_over = True

        # =================================================
        # SNAKE SURVIVES
        # =================================================

        else:

            # Shrink snake ONCE
            snake.shrink()

            # Slow/modify snake speed
            cactus.speedAfterCactusEat(
                snake
            )

            # Find active chickens
            active_chickens = [
                chicken
                for chicken in chickens
                if chicken.active
            ]

            # Put cactus near active chicken
            if active_chickens:

                cactus.random_position(
                    active_chickens[0]
                )

                cactus.active = True

    return score, game_over


# =========================================================
# BANANA COLLISION
# =========================================================

def check_banana_collision(
    snake,
    banana,
    timers,
    banana_sound
):

    if (
        banana.active
        and snake.body[0].colliderect(
            banana.rect
        )
    ):

        # Banana disappears
        banana.eat()

        # Play sound
        banana_sound.play()

        # Change snake speed
        banana.speedAfterEat(
            snake
        )

        # Reset special timers
        timers["special"] = 0
        timers["item_vanish"] = 0