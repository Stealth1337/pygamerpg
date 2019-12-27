import pygame


class Barrier(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.height = height
        self.width = width
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, surface, color, width=0):
        pygame.draw.rect(surface, color, (self.rect.x, self.rect.y, self.width, self.height))
