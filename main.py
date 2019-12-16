import pygame
from room import Room
pygame.init()

width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
fps = 20
clock = pygame.time.Clock()
running = True
c = Room(10, 10, 10, 10)
c.board[0][0] = 1
current_x = 0
current_y = 0
while running:
    screen.fill((0, 0, 0))
    c.render(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                c.board[current_x][current_y] = 0
                c.board[current_x][current_y + 1] = 1
                current_y += 1
            elif event.key == pygame.K_s:
                c.board[current_x][current_y] = 0
                c.board[current_x + 1][current_y] = 1
                current_x += 1
            elif event.key == pygame.K_a:
                c.board[current_x][current_y] = 0
                c.board[current_x][current_y - 1] = 1
                current_y -= 1
            elif event.key == pygame.K_w:
                c.board[current_x][current_y] = 0
                c.board[current_x - 1][current_y] = 1
                current_x -= 1


    clock.tick(fps)
