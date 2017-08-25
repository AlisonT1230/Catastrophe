import pygame
from pygame.locals import FULLSCREEN
import settings
import os
from cat import Cat
from blanket import Blanket
from ground import Ground
from ground_manager import GroundManager
from hud import HUD, HUD_COLOUR
import time

pygame.init()

display = pygame.display.set_mode((settings.screen_width, settings.screen_height), FULLSCREEN)
pygame.display.set_caption('Catastrophe')
clock = pygame.time.Clock()

default_background_col = (255, 255, 255)
black = (0, 0, 0)
boundary_x = 3000
boundary_y = 1000

player = Cat(100, 100, 'black')
hud = HUD()
blankets = [Blanket(300, 575), Blanket(200, 400), Blanket(750, 575)]
ground_manager = GroundManager()
#ground_manager.ground_blocks = [Ground(0, 700, 'wood_planks'), Ground(100, 700, 'wood_planks'), Ground(200, 700, 'wood_planks'), Ground(300, 700, 'stone')]

camera_offset = ((settings.screen_width - player.width)/2 , (settings.screen_height - player.height)/2)  #   offset of bottom left corner of map

#   Initalize sounds
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 512)
#pygame.mixer.music.load(os.path.join("../sounds/music/Catastrophe.wav"))
pygame.mixer.music.load(os.path.join("../sounds/music/Jazzy Cat.wav"))
# --  https://freesound.org/people/soundmary/  -- remove
#player.purr_sound = pygame.mixer.Sound(os.path.join("../sounds/sound_effects/purr.wav"))
player.purr_sound = pygame.mixer.Sound(os.path.join("../sounds/sound_effects/purr_bean.wav"))
#   https://freesound.org/people/Npeo/
player.meow_sound = pygame.mixer.Sound(os.path.join("../sounds/sound_effects/meow.wav"))
player.jump_sound = pygame.mixer.Sound(os.path.join("../sounds/sound_effects/jump.wav"))
player.squeak_sound = pygame.mixer.Sound(os.path.join("../sounds/sound_effects/squeak.wav"))

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
            if pressed[pygame.K_q]:
                pygame.quit()   #   causes error, temporary fullscreen exit
                quit()
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
    player.update(count, boundary_x, boundary_y)
    camera_offset = (450, 350)
    player.update_blanket_val(blankets)
    player.update_ground_val(ground_manager.ground_blocks)
    hud.update(player.health, player.knead_power)


def draw():
    display.blit(player.img, (camera_offset[0], camera_offset[1]))

    for g in ground_manager.ground_blocks:
        display.blit(g.wood_planks, (g.x - player.x + camera_offset[0], g.y - player.y + camera_offset[1]))

    for b in blankets:
        display.blit(b.green_img, (b.x - player.x + camera_offset[0], b.y - player.y + camera_offset[1]))

    display.blit(hud.health_txt, (25, 25))
    display.blit(hud.knead_txt, (25, 45))
    pygame.draw.rect(display, HUD_COLOUR, hud.health_rect)
    pygame.draw.rect(display, HUD_COLOUR, hud.knead_rect)


def load_maps():
    map_0_txt = open("../maps/map_0.txt", "r")
    ground_done = False
    for line in map_0_txt:
        pars = line.split()
        if pars[0] == "--":
            ground_done = True
            continue
        if not ground_done:
            ground_manager.ground_blocks.append(Ground(int(pars[1]), int(pars[2]), pars[0]))
        else:
            blankets.append(Blanket(int(pars[0]), int(pars[1])))

    

    map_0_txt.close()


if __name__ == '__main__':
    load_maps()
    game_loop()

    pygame.quit()
    quit()
    