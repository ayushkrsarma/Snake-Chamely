import pygame

class Help:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        self.image = pygame.image.load(
            "assets/intro/IntroBg.jpg"
        ).convert()

        self.image = pygame.transform.scale(
              self.image,
              (self.width, self.height)
        )

        self.rect = self.image.get_rect()


        # fonts
        self.title_font = pygame.font.Font(
              None,
              70
        )

        self.play_font = pygame.font.Font(
            None,
            40
        )

        self.return_font = pygame.font.Font(
            None,
            40
        )
        self.return_font.set_bold(True)

        self.text_font = pygame.font.Font(
              None,
              36
        )



    def draw(self):

        # background---------
        self.screen.blit(
              self.image,
              self.rect
        )

        # title--------------
        title = self.title_font.render(
            "HOW TO PLAY",
            True,
            (255,255,255)
        )

        title_rect = title.get_rect(
            center=(self.width // 2, 80)
        )

        # play -------------------
        play = self.play_font.render(
            "PLAY TUTORIAL",
            True,
            (255,255,255)
        )

        play_rect = play.get_rect(
            center = (self.width // 2, 440)
        )

        # Return text -------------------
        returnTxt = self.play_font.render(
            "Press RETURN, revert to Start",
            True,
            (255,255,255)
        )  

        returnTxt_rect = returnTxt.get_rect(
            center = (self.width // 2, 680)
        )
        


        self.screen.blit(
            title,
            title_rect
        )

        self.screen.blit(
            play,
            play_rect
        )

        self.screen.blit(
            returnTxt,
            returnTxt_rect
        )



        # Tutorial text
        tutorial = [
          "W - Move Up",
          "S - Move Down",
          "A - Move Left",
          "D - Move Right"
        ]

        tutorial_extra = [
           ["S - Start","H - Help"],
           ["A - About","Q - Quit"]
        ]

        tutorial_play = [
            "Heart - Yields +5 Points, Standardly reswaps in 15 Seconds.",
            "Cactus - Decrements -20 Point, Fixed all along.",
            "Coin - Appers randomly any Cordinate-Interval. Resets Speed to Baseline.",
            "Ruby - Must Figure out by Player :)"

        ]


        # Draw each line
        y = 160

        for line in tutorial:

            text = self.text_font.render(
                line,
                True,
                (255, 255, 255)
            )

            text_rect = text.get_rect(
                center=(self.width // 2, y)
            )

            self.screen.blit(
                text,
                text_rect
            )

            y += 40


        z = 360
        for left_text, right_text in tutorial_extra:

            left = self.text_font.render(
                left_text,
                True,
                (255, 255, 255)
            )

            left_rect = left.get_rect(
                center = (300, z)
            )

            self.screen.blit(
                left,
                left_rect
            )



            # Right side

            right = self.text_font.render(
                right_text,
                True,
                (255, 255, 255)
            )

            right_rect = right.get_rect(
                center = (900, z)
            )


            self.screen.blit(
                right,
                right_rect
            )


            z += 40

        # Draw each line
        k = 500

        for line in tutorial_play:

            text = self.text_font.render(
                line,
                True,
                (170, 242, 170)
            )

            text_rect = text.get_rect(
                center=(self.width // 2, k)
            )

            self.screen.blit(
                text,
                text_rect
            )

            k += 40