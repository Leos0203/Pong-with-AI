import pygame


class Ball:
    def __init__(self, position: pygame.Vector2, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=position)

        self.max_velocity = 600
        self.min_velocity = 300
        self.velocity_x = -self.max_velocity / 2
        self.velocity_y = 0

    def check_collision(self, paddle) -> bool:
        if self.rect.colliderect(paddle):
            return True
        return False

    def update(self, dt) -> None:
        self.rect.x += self.velocity_x * dt
        self.rect.y += self.velocity_y * dt

    def render(self, screen):
        screen.blit(self.image, self.rect)
