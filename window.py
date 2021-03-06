import pygame

class Window:
    def __init__(self, width=500, height=500):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.win = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT], pygame.RESIZABLE)

    def refresh(self, window, box, particles, PGun):
        self.win.fill((255,255,255))
        box.draw(window)
        for p in particles:
            p.draw(window)

        PGun.draw(window)

        pygame.display.update()
