import pygame
from PIL import Image


class StartScreen:

    def __init__(self, screen):

        self.screen = screen

        self.width = screen.get_width()
        self.height = screen.get_height()

        # ---------------- GIF ----------------

        gif = Image.open(
            "assets/intro/greenBack.gif"
        )

        self.frames = []

        for frame_number in range(gif.n_frames):

            gif.seek(frame_number)

            frame = gif.convert("RGBA")

            frame = frame.resize(
                (self.width, self.height)
            )

            # Convert PIL image to bytes
            frame_data = frame.tobytes()

            # Convert bytes to Pygame surface
            pygame_frame = pygame.image.fromstring(
                frame_data,
                frame.size,
                "RGBA"
            )

            self.frames.append(pygame_frame)

        # ---------------- ANIMATION ----------------

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 100

        # ---------------- CHAMELY ----------------

        self.chamely = pygame.image.load(
            "assets/intro/chamely.png"
        ).convert_alpha()

        self.chamely = pygame.transform.scale(
            self.chamely,
            (500, 500)
        )

        # ---------------- FONTS ----------------

        self.title_font = pygame.font.Font(
            None,
            80
        )

        self.button_font = pygame.font.Font(
            None,
            45
        )

    # ==================================================

    def update(self, dt):

        self.frame_timer += dt

        if self.frame_timer >= self.frame_delay:

            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                self.current_frame = 0

            self.frame_timer = 0

    # ==================================================

    def draw(self):

        # Draw animated background
        self.screen.blit(
            self.frames[self.current_frame],
            (0, 0)
        )

        # Draw Chamely
        self.screen.blit(
            self.chamely,
            (360, 85)
        )

        # Title
        title = self.title_font.render(
            "SNAKE CHAMELY",
            True,
            (57, 255, 20)
        )

        # Start
        start_text = self.button_font.render(
            "Start",
            True,
            (255, 255, 255)
        )

        # Help
        help_text = self.button_font.render(
            "Help",
            True,
            (255, 255, 255)
        )

        # About
        about_text = self.button_font.render(
            "About",
            True,
            (255, 255, 255)
        )

        # Quit
        quit_text = self.button_font.render(
            "Quit",
            True,
            (255, 255, 255)
        )

        H_text = self.button_font.render(
            "Press H for Help",
            True,
            (144, 238, 144)
        )

        # Position title
        title_rect = title.get_rect(
            center=(self.width // 2, 100)
        )

        # Position start text
        start_rect = start_text.get_rect(
            center=(self.width // 1.2, 120)
        )

        # Position quit text
        help_rect = help_text.get_rect(
            center=(self.width // 1.2, 180)
        )

        # Position about text
        about_rect = about_text.get_rect(
            center=(self.width // 1.2, 240)
        )

        # Position quit text
        quit_rect = quit_text.get_rect(
            center=(self.width // 1.2, 300)
        )

        H_rect = H_text.get_rect(
            center=(self.width // 2, 700)
        )

        # Draw text
        self.screen.blit(
            title,
            title_rect
        )

        self.screen.blit(
            start_text,
            start_rect
        )

        self.screen.blit(
            help_text,
            help_rect
        )

        self.screen.blit(
            about_text,
            about_rect
        )

        self.screen.blit(
            quit_text,
            quit_rect
        )

        self.screen.blit(
            H_text,
            H_rect
        )