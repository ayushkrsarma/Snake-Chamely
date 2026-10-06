import pygame
import random


class Ruby:

    def __init__(self, screen_width, screen_height):

        self.active = True

        self.image = pygame.image.load(
            "assets/images/ruby.png"
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

    def eat(self, chickens):
        self.active = False
        
        for chicken in chickens:
            chicken.respawn()

        

    def respawn(self):

        self.random_position()
        self.active = True