import pygame


def main():
    app = App()
    app.on_execute()


class App:
    def __init__(self):
        self._running = True
        self.naytto = None
        self.size = (self.weight, self.height) = (800, 600)
 
    def on_execute(self):
        if self.on_init() is False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.tapahtuma(event)
            self.pelilogiikka()
            self.renderointi()

        self.on_cleanup()

    def on_init(self):
        pygame.init()
        self.naytto = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.kuva = pygame.image.load("pallo.png")
        self.kuva_x = 50
        self.kuva_y = 50
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
        if self.kuva_y > 150 and self.putoamisvauhti > 0:
            self.putoamisvauhti = -self.putoamisvauhti
        elif self.kuva_y <= 0 and self.putoamisvauhti < 0:
            self.putoamisvauhti = -self.putoamisvauhti
        self.kuva_y += self.putoamisvauhti

    def renderointi(self):
        self.naytto.fill((100, 100, 200))
        self.naytto.blit(self.kuva, (self.kuva_x, self.kuva_y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 

if __name__ == "__main__" :
    main()
