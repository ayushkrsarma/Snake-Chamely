import pygame
import random



class Banana:

    def __init__(self, screen_width, screen_height):

        self.active = True

        self.image = pygame.image.load(
            "assets/images/banana.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        self.rect = self.image.get_rect()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.random_position()

    def random_position(self):

        self.rect.x = random.randint(
            0,
            self.screen_width - self.rect.width
        )

        self.rect.y = random.randint(
            0,
            self.screen_height - self.rect.height
        )

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, self.rect)

    def eat(self):

        self.active = False

    def respawn(self):

        self.random_position()
        self.active = True

    

    def speedAfterEat(self, snake):
        print("banana hit")
        snake.move_delay = 20
        print("new delay:", snake.move_delay)
        