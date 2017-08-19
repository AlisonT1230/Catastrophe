import pygame
import settings
import global_vars
import os
from cat import Cat
import time

pygame.init()

display = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Catastrophe')
clock = pygame.time.Clock()

player = Cat(100, 100, 'black')
player_img = pygame.image.load(os.path.join(player.img_src))
player_img = pygame.transform.scale(player_img, (100,100))
player_img.convert()

def update():
    player.update()

def game_loop():
    while not global_vars.game_exit:
        display.fill(global_vars.default_background_col)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global_vars.game_exit = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                player.dx = -10
            elif pressed[pygame.K_RIGHT]:
                player.dx = 10
            else:
                player.dx = 0
            if pressed[pygame.K_UP] and player.y == settings.screen_height - player.height:
                player.dy = -20
        update()
        display.blit(player_img, (player.x, player.y))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_loop()

    pygame.quit()
    quit()
    