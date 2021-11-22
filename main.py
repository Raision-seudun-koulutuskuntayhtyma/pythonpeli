import pygame

TAUSTAVARI = (180, 180, 240)  # (Red, Green, Blue), 0...255


def main():
    app = App()
    app.on_execute()


class App:
    def __init__(self):
        self._running = True
        self.naytto = None
        self.nayton_koko = (self.weight, self.height) = (800, 600)
 
    def on_execute(self):
        self.alustus()
 
        while self._running:
            for event in pygame.event.get():
                self.tapahtuma(event)
            self.pelilogiikka()
            self.renderointi()

        self.lopetus()

    def alustus(self):
        pygame.init()
        self.kello = pygame.time.Clock()
        self.naytto = pygame.display.set_mode(
            self.nayton_koko,
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.kuva = pygame.image.load("pallo128.png")
        self.kuvan_koko = self.kuva.get_size()
        self.kuva_x = (self.nayton_koko[0] - self.kuvan_koko[0]) / 2
        self.kuva_y = 50
        self.max_kuva_y = (self.nayton_koko[1] - self.kuvan_koko[1])
        self.putoamisvauhti = 1
 
    def tapahtuma(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.kuva_x -= 10
            elif event.key == pygame.K_RIGHT:
                self.kuva_x += 10

    def pelilogiikka(self):
        self.putoamisvauhti += 0.2
        if self.putoamisvauhti > 10:
            self.putoamisvauhti = 10
        if self.kuva_y > self.max_kuva_y and self.putoamisvauhti > 0:
            self.putoamisvauhti = -self.putoamisvauhti
        self.kuva_y += self.putoamisvauhti

    def renderointi(self):
        self.naytto.fill(TAUSTAVARI)
        self.naytto.blit(self.kuva, (self.kuva_x, self.kuva_y))
        pygame.display.flip()
        self.kello.tick(60)  # 60 fps

    def lopetus(self):
        pygame.quit()
 

if __name__ == "__main__" :
    main()
