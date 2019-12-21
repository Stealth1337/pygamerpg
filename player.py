
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, color):
        pygame.sprite.Sprite.__init__(self)
        self.current_x = start_x
        self.current_y = start_y
        self.player_color = pygame.Color(color)

    def renderPlayer(self, surface):
        pygame.draw.rect(surface, self.player_color, (self.current_x, self.current_y, 30, 30))

    def move(self, event, restriction_list):
        print(restriction_list[3])
        if event == 273:
            if restriction_list[1] < self.current_y:
                self.current_y -= 5
        elif event == 274:
            if self.current_y < restriction_list[3] - 30:
                self.current_y += 5
                print(self.current_y)
        elif event == 276:
            if restriction_list[0] < self.current_x:
                self.current_x -= 5
        elif event == 275:
            if self.current_x < restriction_list[2] - 30:
                self.current_x += 5
