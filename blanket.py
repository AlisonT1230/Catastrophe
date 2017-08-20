import pygame
import os

from tangible import Tangible

class Blanket(Tangible):

    def __init__(self, x, y):
        super(Blanket, self).__init__(x, y, 100, 25)

        #   Load image

        self.green_img = pygame.image.load(os.path.join("textures/blocks/green_blanket.bmp"))
        self.green_img = pygame.transform.scale(self.green_img, (self.width, self.height))
        self.green_img.convert()