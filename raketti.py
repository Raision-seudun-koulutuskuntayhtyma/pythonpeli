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
        self.nappi_pohjassa = False

    def tapahtuma(self, event):
        if event.type == pygame.QUIT:
            self.ajossa = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.nappi_pohjassa = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.nappi_pohjassa = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.pyorimisvauhti = 3
            elif event.key == pygame.K_RIGHT:
                self.pyorimisvauhti = -3
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.pyorimisvauhti = 0

    def pelilogiikka(self):
        if self.nappi_pohjassa:
            self.sijainti = pygame.mouse.get_pos()
        if self.pyorimisvauhti != 0:
            self.kulma = (self.kulma + self.pyorimisvauhti) % 360

    def renderointi(self):
        self.naytto.fill(TAUSTAVARI)
        kuva = pygame.transform.rotozoom(self.kuva_pieni, self.kulma, 1)
        laatikko = kuva.get_rect(center=self.sijainti)
        self.naytto.blit(kuva, laatikko.topleft)
        pygame.display.flip()
        self.kello.tick(60)  # 60 fps (frames per second)

    def lopetus(self):
        pygame.quit()
 

if __name__ == "__main__" :
    main()
