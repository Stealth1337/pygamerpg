import pygame

class Location:

    def __init__(self, start_x, start_y, width, height):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.end_x = start_x + (width * 50)
        self.end_y = start_y + (height * 50)

    def create(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.start_x,
                                                    self.start_y,
                                                    self.width * 50,
                                                    self.height * 50))
