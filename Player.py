import pygame

import Settings


class Player:
    def __init__(self, position: tuple, color, size: pygame.Vector2):
        self.color = color
        self.size = size
        self.rect = pygame.Rect(position, size)

        self.speed = 500

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.rect.y = min(
                self.rect.y + self.speed * dt,
                Settings.SCREEN_HEIGHT - self.size[1] - 16,
            )
        elif keys[pygame.K_w]:
            self.rect.y = max(self.rect.y - self.speed * dt, 16)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
