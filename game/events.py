import pygame

def handle_events(game_state, running, snake, about_screen):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif game_state == "start":

            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_s, pygame.K_RETURN):
                    game_state = "game"

                elif event.key == pygame.K_h:
                    game_state = "help"

                elif event.key == pygame.K_a:
                    game_state = "about"

                elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False

        elif game_state == "help":

            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                    game_state = "start"

                # elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                #     running = False

        elif game_state == "about":

            # IMPORTANT: event exists here
            about_screen.handle_event(event)

            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                    game_state = "start"

                # elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                #     running = False

        elif game_state == "game":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    snake.direction = pygame.Vector2(0, -1)

                elif event.key == pygame.K_s:
                    snake.direction = pygame.Vector2(0, 1)

                elif event.key == pygame.K_a:
                    snake.direction = pygame.Vector2(-1, 0)

                elif event.key == pygame.K_d:
                    snake.direction = pygame.Vector2(1, 0)

                elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                    game_state = "start"

    return running, game_state