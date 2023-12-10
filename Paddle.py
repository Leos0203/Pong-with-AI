import pygame


class Paddle:
    def __init__(self, position: tuple, color, size: pygame.Vector2):
        self.color = color
        self.size = size
        self.rect = pygame.Rect(position, size)

        self.speed = 500

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
