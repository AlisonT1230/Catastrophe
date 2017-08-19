import pygame
import settings
import os
from cat import Cat
import time

pygame.init()

display = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Catastrophe')
clock = pygame.time.Clock()

default_background_col = (255, 255, 255)
black = (0, 0, 0)

player = Cat(100, 100, 'black')
player_img = pygame.image.load(os.path.join(player.img_src))
player_img = pygame.transform.scale(player_img, (100,100))
player_img.convert()

def update():
    player.update()

def game_loop():
    game_exit = False
    while not game_exit:
        display.fill(default_background_col)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                player.move_left()
            elif pressed[pygame.K_RIGHT]:
                player.move_right()
            else:
                player.stop()
            if pressed[pygame.K_UP]:
                player.jump()
            elif pressed[pygame.K_DOWN]:
                player.knead()
        update()
        display.blit(player_img, (player.x, player.y))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_loop()

    pygame.quit()
    quit()
    