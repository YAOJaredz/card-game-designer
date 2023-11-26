import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.rendered_text = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def update(self, surface):
        surface.blit(self.rendered_text, self.text_rect)

class Label(pygame.sprite.Sprite):
    def __init__(self, x, y, text, font_size, color=(0,0,0)):
        super().__init__()
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.color = color
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)