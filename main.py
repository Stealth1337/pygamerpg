import pygame
from location import Location
from player import Player

pygame.init()

size_screen = width, height = 800, 600
main_screen = pygame.display.set_mode(size_screen)
running_game = True

location_1 = True
loc_1 = Location(0, 0, 5, 5)
location_screen = pygame.Surface((loc_1.width * 50, loc_1.height * 50))
loc_1.create(location_screen)
player = Player(20, 20, 'red')

while running_game:
    main_screen.fill((0, 0, 0))
    player.renderPlayer(location_screen)
    main_screen.blit(location_screen, (10, 10))
    location_screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
        elif event.type == pygame.KEYDOWN:
                player.move(event.key, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
                print(player.current_x)
                print(loc_1.end_x)
    pygame.display.flip()
pygame.quit()