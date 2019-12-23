import pygame
from location import Location
from player import Player
from barriers import Barrier

pygame.init()

size_screen = width, height = 800, 600
main_screen = pygame.display.set_mode(size_screen)
running_game = True

FPS = 30
clock = pygame.time.Clock()
location_1 = True
loc_1 = Location(0, 0, 10, 10)
location_screen = pygame.Surface((loc_1.width * 50, loc_1.height * 50))
loc_1.create(location_screen)
all_sprites = pygame.sprite.Group()
player = Player(20, 20, 'red')
barrier1 = Barrier(100, 100, 1, 1)
while running_game:
    main_screen.fill((0, 0, 0))
    player.renderPlayer(location_screen)
    barrier1.render(location_screen, (255, 255, 0))
    main_screen.blit(location_screen, (10, 10))
    location_screen.fill((255, 255, 255))
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
    keys = pygame.key.get_pressed()
    hit = pygame.sprite.collide_rect(player, barrier1)
    if hit and (barrier1.rect.y + barrier1.height) - player.rect.y < barrier1.height and keys[pygame.K_UP]:
        pass
    elif hit and 0 <= (player.rect.y + 30 - barrier1.rect.y) <= 5 and keys[pygame.K_DOWN]:
        pass
    elif hit and (barrier1.rect.x - player.rect.x - 30) <= 0 and 0 <= (player.rect.y + 30 - barrier1.rect.y) <= barrier1.width + 30 and keys[pygame.K_RIGHT]:
        pass
    elif keys[pygame.K_UP]:
        player.move(pygame.K_UP, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        print('barrier1', barrier1.rect.x, barrier1.rect.y)
        print('player', player.rect.x, player.rect.y)
    elif keys[pygame.K_DOWN]:
        player.move(pygame.K_DOWN, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        print('barrier1', barrier1.rect.x, barrier1.rect.y)
        print('player', player.rect.x, player.rect.y)
    elif keys[pygame.K_LEFT]:
        player.move(pygame.K_LEFT, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        print('barrier1', barrier1.rect.x, barrier1.rect.y)
        print('player', player.rect.x, player.rect.y)
    elif keys[pygame.K_RIGHT]:
        player.move(pygame.K_RIGHT, [loc_1.start_x, loc_1.start_y, loc_1.end_x, loc_1.end_y])
        print('barrier1', barrier1.rect.x, barrier1.rect.y)
        print('player', player.rect.x, player.rect.y)
        print((barrier1.rect.x - player.rect.x - 30))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
