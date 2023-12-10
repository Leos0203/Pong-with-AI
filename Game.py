import pygame

import Settings
from Ball import Ball
from Paddle import Paddle


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.line = pygame.image.load("border.png")

        self.Player = Paddle((32, 200), (0, 255, 255), (12, 64))
        self.Enemy = Paddle((Settings.SCREEN_WIDTH - 32, 200), (204, 0, 0), (12, 64))

        self.Borders = [
            pygame.Rect(0, 0, Settings.SCREEN_WIDTH, 16),
            pygame.Rect(0, Settings.SCREEN_HEIGHT - 16, Settings.SCREEN_WIDTH, 16),
        ]

        self.Ball = Ball((Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT / 2), "ball.png")
        self.ball_collision_timer = 0

        self.score = [0, 0]
        self.font = pygame.font.SysFont("Roboto", 64)

    def ball_paddle_collision(self, paddle: Paddle):
        if pygame.time.get_ticks() - paddle.collision_timer >= 10:
            if self.Ball.check_collision(paddle.rect):
                # paddle size is 64 so value is in range -32 to 32
                interesect = paddle.rect.center[1] - self.Ball.rect.y
                # this will give us a value between -1 and 1
                normalized_intersect = interesect / 32
                if self.Ball.velocity_x > 0:
                    self.Ball.velocity_x = max(-self.Ball.min_velocity, -self.Ball.max_velocity * normalized_intersect)
                elif self.Ball.velocity_x < 0:
                    self.Ball.velocity_x = max(self.Ball.min_velocity, self.Ball.max_velocity * normalized_intersect)
                self.Ball.velocity_y = self.Ball.max_velocity * -normalized_intersect
            paddle.collision_timer = pygame.time.get_ticks()

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

    def AI_algorythm(self, dt):
        if self.Ball.rect.y < self.Enemy.rect.y:
            self.Enemy.rect.y = max(self.Enemy.rect.y - self.Enemy.speed * dt, 16)
        if self.Ball.rect.y > self.Enemy.rect.y:
            self.Enemy.rect.y = min(
                self.Enemy.rect.y + self.Enemy.speed * dt, Settings.SCREEN_HEIGHT - self.Enemy.size[1] - 16
            )

    def update(self, dt):
        self.team_one_score_text = self.font.render(f"{self.score[0]}", True, (255, 255, 255))
        self.team_two_score_text = self.font.render(f"{self.score[1]}", True, (255, 255, 255))
        self.check_for_point()
        self.ball_paddle_collision(self.Player)
        self.ball_paddle_collision(self.Enemy)

        for border in self.Borders:
            if self.Ball.check_collision(border):
                self.Ball.velocity_y *= -1

        self.AI_algorythm(dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.Player.rect.y = min(
                self.Player.rect.y + self.Player.speed * dt, Settings.SCREEN_HEIGHT - self.Player.size[1] - 16
            )
        elif keys[pygame.K_w]:
            self.Player.rect.y = max(self.Player.rect.y - self.Player.speed * dt, 16)

        self.Ball.update(dt)

    def render(self):
        self.screen.blit(self.line, (Settings.SCREEN_WIDTH / 2, 0))
        self.screen.blit(self.team_one_score_text, (Settings.SCREEN_WIDTH / 2 - 60, 30))
        self.screen.blit(self.team_two_score_text, (Settings.SCREEN_WIDTH / 2 + 50, 30))

        for border in self.Borders:
            pygame.draw.rect(self.screen, (224, 224, 224), border)

        self.Player.render(self.screen)
        self.Enemy.render(self.screen)

        self.Ball.render(self.screen)
