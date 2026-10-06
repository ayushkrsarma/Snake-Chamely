import pygame

class Snake:

    def __init__(self):
        self.block_size = 20

        self.screen_width = 1280
        self.screen_height = 720

        self.move_delay = 20

        self.body = [
            pygame.Rect(300, 300, self.block_size, self.block_size),
            pygame.Rect(280, 300, self.block_size, self.block_size),
            pygame.Rect(260, 300, self.block_size, self.block_size)
        ]

        self.direction = pygame.Vector2(1, 0)

    def move(self):
        new_head = self.body[0].copy()

        new_head.x += self.direction.x * self.block_size
        new_head.y += self.direction.y * self.block_size

        # Screen wrapping

        # RIGHT -> LEFT
        if new_head.x >= self.screen_width:
            new_head.x = 0

        # DOWN -> UP
        if new_head.x < 0:
            new_head.x = self.screen_width - self.block_size

        # UP -> BUTTOM
        if new_head.y < 0:
            new_head.y = self.screen_height - self.block_size

        if new_head.y >= self.screen_height:
            new_head.y = 0

        self.body.insert(0, new_head)

        self.body.pop()

    def grow(self):
        new_tail = self.body[-1].copy()
        self.body.append(new_tail)

    def shrink(self):
        if len(self.body) > 1:
            self.body.pop()