import pygame

class Location:

    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


    def create(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.start_x,
                                                    self.start_y,
                                                    self.end_x,
                                                    self.end_y))