import pygame


class Room:
    # создание поля
    def __init__(self, width, height, left, top):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = left
        self.top = top
        self.cell_size = 50

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                rect = pygame.Rect(self.left + j * self.cell_size,
                                   self.top + i * self.cell_size,
                                   self.cell_size,
                                   self.cell_size)
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (self.left + j * self.cell_size + self.cell_size // 2,
                                        self.top + i * self.cell_size + self.cell_size // 2),
                                       10)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.left or mouse_pos[1] < self.top or \
                mouse_pos[0] > self.left + (self.width * self.cell_size) or \
                mouse_pos[1] > self.top + (self.height * self.cell_size):
            return None
        else:
            return ((mouse_pos[0] - self.left) // self.cell_size), \
                   ((mouse_pos[1] - self.top) // self.cell_size)
