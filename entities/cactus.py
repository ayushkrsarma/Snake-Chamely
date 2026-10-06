import pygame
import random


class Cactus:

    def __init__(self, screen_width, screen_height):

        self.points = -20
        self.active = True

        self.image = pygame.image.load(
            "assets/images/cactus.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        self.rect = self.image.get_rect()

        self.screen_width = screen_width
        self.screen_height = screen_height

       


    def random_position(self, chicken):

        distance = 150

        self.rect.x = random.randint(
            max(0, chicken.rect.x - distance),
            min(
                self.screen_width - self.rect.width,
                chicken.rect.x + distance
            )
        )

        self.rect.y = random.randint(
            max(0, chicken.rect.y - distance),
            min(
                self.screen_height - self.rect.height,
                chicken.rect.y + distance
            )
        )


    def draw(self, screen):

        if self.active:
            screen.blit(self.image, self.rect)


    def eat(self):

        self.active = False


    def respawn(self, chicken):

        self.random_position(chicken)
        self.active = True


    def speedAfterCactusEat(self, snake):

        print("cactus hit")

        snake.move_delay = 3

        print("new delay:", snake.move_delay)