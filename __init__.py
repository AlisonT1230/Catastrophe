import pygame
import settings
import os
from cat import Cat
import time

pygame.init()

display = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Catastrophe')
clock = pygame.time.Clock()

game_exit = False
default_background_col = (255, 255, 255)
black = (0, 0, 0)

bean = Cat(100, 100, 'black')
bean_img = pygame.image.load(os.path.join(bean.img_src))
bean_img = pygame.transform.scale(bean_img, (100,100))
bean_img.convert()

while not game_exit:
    display.fill(default_background_col)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            bean.dx = -5
        elif pressed[pygame.K_RIGHT]:
            bean.dx = 5
        else:
            bean.dx = 0
        if pressed[pygame.K_UP]:
            bean.dy = -15
        
    bean.update()
    display.blit(bean_img, (bean.x, bean.y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()