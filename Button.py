class Button:
    def __init__(self, font, text, antialias, x, y, color) -> None:
        self.antialias = antialias
        self.text = text
        self.color = color

        self.surface = font.render(self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect(topleft=(x, y))

    def check_collidepoint(self, position) -> bool:
        if self.rect.collidepoint(position):
            return True
        return False

    def render(self, screen):
        screen.blit(self.surface, self.rect)
