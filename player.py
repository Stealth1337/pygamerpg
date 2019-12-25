
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, color):
        pygame.sprite.Sprite.__init__(self)
        self.player_color = pygame.Color(color)
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def renderPlayer(self, surface):
        pygame.draw.rect(surface, self.player_color, (self.rect.x, self.rect.y, 30, 30))

    def move(self, event, restriction_list):
        if event == pygame.K_UP:
            if restriction_list[1] < self.rect.y:
                self.rect.y -= 5
        elif event == pygame.K_DOWN:
            if self.rect.y < restriction_list[3] - 30:
                self.rect.y += 5
        elif event == pygame.K_LEFT:
            if restriction_list[0] < self.rect.x:
                self.rect.x -= 5
        elif event == pygame.K_RIGHT:
            if self.rect.x < restriction_list[2] - 30:
                self.rect.x += 5


class PlayerBorders(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.add(group)

    def update(self, screen, key):
        if key == pygame.K_RIGHT:
            self.rect.x += 5
        elif key == pygame.K_LEFT:
            self.rect.x -= 5
        elif key == pygame.K_UP:
            self.rect.y -= 5
        elif key == pygame.K_DOWN:
            self.rect.y += 5


