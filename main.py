import pygame
from location import Location
from player import Player, PlayerBorders
from barriers import Barrier

pygame.init()

size_screen = width, height = 800, 600
main_screen = pygame.display.set_mode(size_screen)
running_game = True

# main info

all_sprites = pygame.sprite.Group()
FPS = 30
clock = pygame.time.Clock()

# location info

location_1 = True
loc_1 = Location(0, 0, 10, 10)
location_screen = pygame.Surface((loc_1.width * 50, loc_1.height * 50))
loc_1.create(location_screen)

# Sprites

all_sprites = pygame.sprite.Group()

# player sprites and borders

player = Player(20, 20, 'red')
all_sprites.add(player)
borders = pygame.sprite.Group()
all_sprites.add(borders)
left_border = PlayerBorders(player.rect.x - 1, player.rect.y, 1, 30, borders)
right_border = PlayerBorders(player.rect.x + 30, player.rect.y, 1, 30, borders)
up_border = PlayerBorders(player.rect.x, player.rect.y - 1, 30, 1, borders)
down_border = PlayerBorders(player.rect.x, player.rect.y + 30, 30, 1, borders)

#

barrier_objects = pygame.sprite.Group()
barrier1 = Barrier(100, 100, 1, 1)
barrier2 = Barrier(150, 150, 2, 2)
barrier_objects.add(barrier1)
barrier_objects.add(barrier2)
all_sprites.add(barrier_objects)

while running_game:
    main_screen.fill((0, 0, 0))
    #
    player.renderPlayer(location_screen)
    borders.draw(location_screen)
    #
    barrier_objects.update(location_screen, (255, 255, 0))
    #
    main_screen.blit(location_screen, (10, 10))
    location_screen.fill((255, 255, 255))
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
    keys = pygame.key.get_pressed()

    if pygame.sprite.spritecollideany(left_border, barrier_objects) and keys[pygame.K_LEFT]:
        pass
    elif pygame.sprite.spritecollideany(right_border, barrier_objects) and keys[pygame.K_RIGHT]:
        pass
    elif pygame.sprite.spritecollideany(up_border, barrier_objects) and keys[pygame.K_UP]:
        pass
    elif pygame.sprite.spritecollideany(down_border, barrier_objects) and keys[pygame.K_DOWN]:
        pass
    elif keys[pygame.K_UP]:
        player.move(pygame.K_UP, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        borders.update(location_screen, pygame.K_UP)
    elif keys[pygame.K_DOWN]:
        player.move(pygame.K_DOWN, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        borders.update(location_screen, pygame.K_DOWN)
    elif keys[pygame.K_LEFT]:
        player.move(pygame.K_LEFT, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        borders.update(location_screen, pygame.K_LEFT)
    elif keys[pygame.K_RIGHT]:
        player.move(pygame.K_RIGHT, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        borders.update(location_screen, pygame.K_RIGHT)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
