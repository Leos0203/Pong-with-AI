import sys

import pygame

import Settings
from Button import Button


class Menu:
    def __init__(self, screen) -> None:
        self.screen = screen

        self.font = pygame.font.SysFont("Roboto", 80)
        self.start_button = Button(
            self.font,
            "Start",
            True,
            Settings.SCREEN_WIDTH / 2 - 70,
            Settings.SCREEN_HEIGHT / 2 - 50,
            (255, 255, 255),
        )
        self.exit_button = Button(
            self.font,
            "Exit",
            True,
            Settings.SCREEN_WIDTH / 2 - 60,
            Settings.SCREEN_HEIGHT / 2 + 50,
            (255, 255, 255),
        )

        self.switch_to_game = False

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            if self.exit_button.check_collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            elif self.start_button.check_collidepoint(pygame.mouse.get_pos()):
                self.switch_to_game = True

    def render(self):
        self.start_button.render(self.screen)
        self.exit_button.render(self.screen)
