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

pygame.mixer.pre_init(44100, -16, 2, 4096)
music = pygame.mixer.music.load("sounds/music/catastrophe.wav")

def game_loop():
    game_exit = False
    count = 0
    pygame.mixer.music.play(-1)
    while not game_exit:
        display.fill(default_background_col)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            #pressed = pygame.key.get_pressed()
            #if pressed[pygame.K_LEFT]:
            #    player.move_left()
            #elif pressed[pygame.K_RIGHT]:
            #    player.move_right()
            #else:
            #    player.stop()
            #if pressed[pygame.K_UP]:
            #    player.jump()
            #elif pressed[pygame.K_DOWN]:
            #    player.knead()
            #
            #if not pressed[pygame.K_DOWN]:
            #    player.stop_knead()
        
        cursor_x = pygame.mouse.get_pos()[0]
        cursor_y = pygame.mouse.get_pos()[1]
        
        update(count, cursor_x, cursor_y)
        draw()

        pygame.display.update()
        clock.tick(60)
        if count == 100:
            count = 0
        else:
            count += 1

def update(count, cursor_x, cursor_y):
    player.update(count, cursor_x, cursor_y)

def draw():
    display.blit(player.img, (player.x, player.y))

if __name__ == '__main__':
    game_loop()

    pygame.quit()
    quit()
    