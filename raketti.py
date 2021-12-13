import pygame

TAUSTAVARI = (180, 180, 240)  # (Red, Green, Blue), 0...255


def main():
    peli = Peli()
    peli.aja()


class Peli:
    def __init__(self):
        self.ajossa = True
        self.naytto = None
        self.leveys = 800
        self.korkeus = 600
        self.nayton_koko = (self.leveys, self.korkeus)
 
    def aja(self):
        self.alustus()
        while self.ajossa:
            for event in pygame.event.get():
                self.tapahtuma(event)
            self.pelilogiikka()
            self.renderointi()
        self.lopetus()

    def alustus(self):
        pygame.init()
        self.kello = pygame.time.Clock()
        self.naytto = pygame.display.set_mode(
            self.nayton_koko, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.kuva_iso = pygame.image.load("rocket_883.png")
        self.kuva_pieni = pygame.transform.rotozoom(self.kuva_iso, 0, 0.25)
        self.kulma = 0
        self.pyorimisvauhti = 0
        self.sijainti = (400, 300)
        self.hiiren_nappi_pohjassa = False
        self.voima = 0
        self.voimanlisays = False
        self.laukaisu = False

    def tapahtuma(self, event):
        if event.type == pygame.QUIT:
            self.ajossa = False
        # Hiiren tapahtumat --------------------------------------
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.hiiren_nappi_pohjassa = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.hiiren_nappi_pohjassa = False
        # Näppäimen painaminen alas ------------------------------
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.pyorimisvauhti = 3
            elif event.key == pygame.K_RIGHT:
                self.pyorimisvauhti = -3
            elif event.key == pygame.K_SPACE:
                self.voimanlisays = True
        # Näppäimen nosto ylös  ----------------------------------
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.pyorimisvauhti = 0
            elif event.key == pygame.K_SPACE:
                self.voimanlisays = False
                self.laukaisu = True

    def pelilogiikka(self):
        if self.hiiren_nappi_pohjassa:
            self.sijainti = pygame.mouse.get_pos()

        if self.pyorimisvauhti != 0:
            self.kulma = (self.kulma + self.pyorimisvauhti) % 360

        if self.voimanlisays:
            self.voima = min(self.voima + 1, 100)

        if self.laukaisu:
            print(f"Pam! {self.voima}")
            self.voima = 0
            self.laukaisu = False

    def renderointi(self):
        self.naytto.fill(TAUSTAVARI)
        kuva = pygame.transform.rotozoom(self.kuva_pieni, self.kulma, 1)
        laatikko = kuva.get_rect(center=self.sijainti)
        self.naytto.blit(kuva, laatikko.topleft)
        pygame.draw.rect(self.naytto, (0, 0, 0), (2, self.korkeus - 19, 102, 17))
        pygame.draw.rect(self.naytto, (0, 255, 0), (3, self.korkeus - 18, self.voima, 15))
        pygame.display.flip()
        self.kello.tick(60)  # 60 fps (frames per second)

    def lopetus(self):
        pygame.quit()
 

if __name__ == "__main__" :
    main()
