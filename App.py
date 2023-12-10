import sys

import pygame

from Game import Game
from Menu import Menu


class App:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((858, 525))
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.Menu = Menu(self.screen)
        self.Game = Game(self.screen)

        self.in_game = False

    def update(self):
        if self.Menu.switch_to_game:
            self.in_game = True

        if self.in_game:
            self.Game.update(self.dt)
        else:
            self.Menu.update()

    def render(self):
        if self.in_game:
            self.Game.render()
        else:
            self.Menu.render()

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
