import pygame


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width * 50
        self.height = height * 50

    def render(self, surface, color):
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
