import sys

import pygame


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((858, 525))
        self.clock = pygame.time.Clock()
        self.dt = 0

    def update(self):
        pass

    def render(self):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")

            self.update()
            self.render()

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
