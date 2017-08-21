import pygame
import settings
import os
from cat import Cat
from blanket import Blanket
from hud import HUD, HUD_COLOUR
import time

pygame.init()

display = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Catastrophe')
clock = pygame.time.Clock()

default_background_col = (255, 255, 255)
black = (0, 0, 0)

player = Cat(100, 100, 'black')
blanket = Blanket(300, 575)
hud = HUD()

#   Initalize sounds
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 512)
music = pygame.mixer.music.load(os.path.join("sounds/music/Catastrophe.wav"))
#   https://freesound.org/people/soundmary/
player.purr_sound = pygame.mixer.Sound(os.path.join("sounds/sound_effects/purr.wav"))
#   https://freesound.org/people/Npeo/
player.meow_sound = pygame.mixer.Sound(os.path.join("sounds/sound_effects/meow.wav"))
player.jump_sound = pygame.mixer.Sound(os.path.join("sounds/sound_effects/jump.wav"))

def game_loop():
    game_exit = False
    count = 0
    pygame.mixer.music.play(-1)
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
                if not player.kneading:
                    player.knead()
            
            if not pressed[pygame.K_DOWN]:
                player.stop_knead()

        update(count)
        draw()

        pygame.display.update()
        clock.tick(60)
        if count == 100:
            count = 0
        else:
            count += 1


def update(count):
    player.update(count)
    player.update_blanket_val(blanket)
    hud.update(player.health, player.knead_power)


def draw():
    display.blit(player.img, (player.x, player.y))
    display.blit(blanket.green_img, (blanket.x, blanket.y))
    display.blit(hud.health_txt, (25, 25))
    display.blit(hud.knead_txt, (25, 45))
    pygame.draw.rect(display, HUD_COLOUR, hud.health_rect)
    pygame.draw.rect(display, HUD_COLOUR, hud.knead_rect)

if __name__ == '__main__':
    game_loop()

    pygame.quit()
    quit()
    