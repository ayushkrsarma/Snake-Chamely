import pygame


class About:

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

        self.title_font = pygame.font.Font(
            None,
            70
        )

        self.story_font = pygame.font.Font(
            None,
            40
        )

        self.scroll_y = 0
        self.scroll_speed = 40

        self.story = """Prachin Magdaha ke Rajdhani me eak atynat 
            roopvati Chamely naamak kanya niwas karti thi
            Chameli ko chankya ne 
            vishknaya me shaamil kar liya tha
            Chamely apne kaam ko bahut safai se karti thi
            Uska vish halahal se bhi gehra tha.

            Usne roop ke jaal fekakr kai shikar fasyae...
            Par ant me sabka ant hota hi hai

            Kaal kisi Brishpati ke din Dhanwan 
            mani ka saudagar banker 
            Magadh ke tang galiyo me ghumta 
            Uske paas Manik/Ruby ka eak potli tha

            Chamely ki nazar uspar padi 
            Usne lalach me aakar uss vypari ke picche pad gai


            *       *        *
            saiyan hai vyapari
            Chale hai pardesh
            Suratiya niharu
            Jiyara bhaari hove

            Sasural, sasural
            Sasural genda phool
            *       *        *
            


            Aakhir uski mehant rang laai raat ke 4th pahar, Usha me
            Shikar phas hi gya yaa Shikari khud phas gya.

            Chamely vishknya ne use jaal me fasa liya tha
            Shikar bahut chanchl tha, aur bahut hi Utavala
            Intejaar to tha hi nahi usme...

            Chamealy uske nazdik aa gai
            aur, aur, aur, aur, aur, aur nazdik
            saanso ki grami ab hawa me mahsoos hone lagi thi

            Chamely ne pahle se hi uski dhadkan rok rakhi thi
            Karib jaane par to band hi ho gaya
            Usne uske hirday par haath rakha


            -------------------------------------
            Hirady ki awaz shaant thi
            Chamely ka haat uske hirday pe tha
            -------------------------------------
            Hirday Garam tha
            Chmaely ka sparsh tha
            -------------------------------------
            Hirday bekarar tha
            Chmely ka sparsh aanshik tha
            -------------------------------------
            Hirday Ashantust tha
            Chamely ka sparsh mombati thi
            -------------------------------------
            Hirday Shantust tha 
            Chamely ka sparsh Agni tha
            --------------------------------------

            Eak hi pal me hirday chaati se bahhar tha
            Chamely ki haath khun se range huye the
            Usne hirday ko apne daant se nochkar apne vish se band kar diya

            usne daat se nochkar ruby nikal bagal me padi potli se
            aur hirday ke tukde ke saath nigal gai



            USI SAMAY SABKUCH UZALA HO GYA
            AUR SUNYA SE BHWAISHYWANI HUI-

            
           
           
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            TU ANNANT KAAL KE LIYE WAHI
            PEEDA-DUKH-KASTH-VIPATI-DARD-SANTAP-
            SHOK-VAYTHA-KLESH-MIRTYU-SHARAP
            MAHSOOS KAREGI
            JO TUNE ANGINAT LOGO KO DIYA
            UNKA MAANS KHAYA, AB TERI BAARI HAI
            JSIKI TUJHE PYAS THI, MAANS AUR PATHAR
            <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
           

            CHAMELY KO MANIK/RUBY CHAHIYE TABHI USKO MUKTI MILEGI
            USKI MUKTI IN PATHRO ME UZLHI PADI HAI

            KAAL SE KOI BACH SAKA HAI
            JO MAIN BACHUNGI LEKIN
            AB MERI BARI HAI
            MAIN APNE PARARABDH KE LIYE TAIYAR HU
            MAIN APNI MUKTI KE LIYE TAIYAR HU
            *            *               *

            ISLIYE KAUTILYA NE KAHA HAI - 
            "Lobhashchedagunena kim pishunata yadyasti kim patakaih".
            ISI PAR ISWARN KAHTA HAI - 
            "NEVER - EVER BE A BUSINESS WOEMEN!"


            

            ################################

            AUTHOR - ISWARAN
            Snake Chamely - MARK I

            ################################

            

            """





    def wrap_text(self, text, max_width):

        lines = []

        # Process each \n separately
        paragraphs = text.split("\n")

        for paragraph in paragraphs:

            # Preserve blank lines
            if paragraph.strip() == "":
                lines.append("")
                continue

            # Count tabs at the beginning
            tab_count = len(paragraph) - len(paragraph.lstrip("\t"))

            # Remove tabs before word wrapping
            paragraph = paragraph.lstrip("\t")

            words = paragraph.split()

            current_line = ""

            for word in words:

                test_line = current_line + " " + word

                if self.story_font.size(test_line)[0] <= max_width:
                    current_line = test_line.strip()

                else:

                    if current_line:
                        lines.append(
                            "\t" * tab_count + current_line
                        )

                    current_line = word

            if current_line:
                lines.append(
                    "\t" * tab_count + current_line
                )

        return lines


    def handle_event(self, event):

      if event.type == pygame.MOUSEWHEEL:

            self.scroll_y -= event.y * self.scroll_speed

            # Create wrapped lines
            lines = self.wrap_text(
                self.story,
                self.width - 150
            )

            # Total height of wrapped story
            content_height = len(lines) * 50

            # Visible story area
            visible_height = self.height - 150

            # Maximum scrolling distance
            max_scroll = max(
                0,
                content_height - visible_height
            )

            # Don't scroll above beginning
            if self.scroll_y > 0:
                self.scroll_y = 0

            # Don't scroll below ending
            if self.scroll_y < -max_scroll:
                self.scroll_y = -max_scroll


    def draw(self):

        # -----------------
        # BACKGROUND
        # -----------------

        self.screen.blit(
            self.image,
            self.rect
        )


        # -----------------
        # TITLE
        # -----------------

        title = self.title_font.render(
            "STORY",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(self.width // 2 , 80)
        )

        self.screen.blit(
            title,
            title_rect
        )


        # -----------------
        # WRAP STORY
        # -----------------

        lines = self.wrap_text(
            self.story,
            self.width - 150
        )


        # -----------------
        # STORY AREA
        # -----------------

        story_area = pygame.Rect(
            50,
            130,
            self.width - 100,
            self.height - 130
        )

        self.screen.set_clip(story_area)


        # -----------------
        # DRAW STORY
        # -----------------

        y = 150 + self.scroll_y

        for line in lines:

            story = self.story_font.render(
                line,
                True,
                (255, 255, 255)
            )

            story_rect = story.get_rect(
                center=(self.width // 2, y)
            )

            self.screen.blit(
                story,
                story_rect
            )

            y += 50


        # Remove clipping
        self.screen.set_clip(None)


        # -----------------
        # SCROLLBAR
        # -----------------

        content_height = len(lines) * 50

        visible_height = self.height - 150

        if content_height > visible_height:

            scrollbar_height = max(
                50,
                int(
                    visible_height
                    * visible_height
                    / content_height
                )
            )

            max_scroll = content_height - visible_height

            scrollbar_y = int(
                (-self.scroll_y / max_scroll)
                * (visible_height - scrollbar_height)
            )

            pygame.draw.rect(
                self.screen,
                (100, 100, 100),
                (
                    self.width - 15,
                    130 + scrollbar_y,
                    10,
                    scrollbar_height
                )
            )