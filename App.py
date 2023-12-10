import math
import sys

import pygame

import Settings
from Ball import Ball
from Player import Player


class App:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((858, 525))
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.line = pygame.image.load("border.png")

        self.Player = Player((32, 200), (255, 255, 255), (12, 64))

        self.Borders = [
            pygame.Rect(0, 0, Settings.SCREEN_WIDTH, 16),
            pygame.Rect(0, Settings.SCREEN_HEIGHT - 16, Settings.SCREEN_WIDTH, 16),
        ]

        self.Ball = Ball((Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT / 2), "ball.png")
        self.ball_collision_timer = 0

        self.score = [0, 0]
        self.font = pygame.font.SysFont("Roboto", 64)

    def collision(self):
        if pygame.time.get_ticks() - self.ball_collision_timer >= 10:
            if self.Ball.check_collision(self.Player.rect):
                # paddle size is 64 so value is in range -32 to 32
                interesect = self.Player.rect.center[1] - self.Ball.rect.y
                # this will give us a value between -1 and 1
                normalized_intersect = interesect / 32
                self.Ball.velocity_x = max(self.Ball.min_velocity, self.Ball.max_velocity * normalized_intersect)
                self.Ball.velocity_y = self.Ball.max_velocity * -normalized_intersect

            for border in self.Borders:
                if self.Ball.check_collision(border):
                    self.Ball.velocity_y *= -1
            self.ball_collision_timer = pygame.time.get_ticks()

    def check_for_point(self):
        if self.Ball.rect.x < -self.Ball.image.get_size()[0]:
            self.Ball.rect.topleft = (Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT / 2)
            self.ball_collision_timer = 0
            self.score[1] += 1
            self.Ball.velocity_x = -self.Ball.max_velocity / 2
            self.Ball.velocity_y = 0
        if self.Ball.rect.x > Settings.SCREEN_WIDTH:
            self.Ball.rect.topleft = (Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT / 2)
            self.ball_collision_timer = 0
            self.score[0] += 1
            self.Ball.velocity_x = self.Ball.max_velocity / 2
            self.Ball.velocity_y = 0

    def update(self):
        self.team_one_score_text = self.font.render(f"{self.score[0]}", True, (255, 255, 255))
        self.team_two_score_text = self.font.render(f"{self.score[1]}", True, (255, 255, 255))
        self.check_for_point()
        self.collision()

        self.Player.update(self.dt)
        self.Ball.update(self.dt)

    def render(self):
        self.screen.blit(self.line, (Settings.SCREEN_WIDTH / 2, 0))
        self.screen.blit(self.team_one_score_text, (Settings.SCREEN_WIDTH / 2 - 60, 30))
        self.screen.blit(self.team_two_score_text, (Settings.SCREEN_WIDTH / 2 + 50, 30))

        for border in self.Borders:
            pygame.draw.rect(self.screen, (224, 224, 224), border)

        self.Player.render(self.screen)

        self.Ball.render(self.screen)

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
