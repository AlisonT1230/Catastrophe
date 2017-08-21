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

        self.blue_img = pygame.image.load(os.path.join("textures/blocks/blue_blanket.bmp"))
        self.blue_img = pygame.transform.scale(self.blue_img, (self.width, self.height))
        self.blue_img.convert()

        self.purple_img = pygame.image.load(os.path.join("textures/blocks/purple_blanket.bmp"))
        self.purple_img = pygame.transform.scale(self.purple_img, (self.width, self.height))
        self.purple_img.convert()

        self.red_img = pygame.image.load(os.path.join("textures/blocks/red_blanket.bmp"))
        self.red_img = pygame.transform.scale(self.red_img, (self.width, self.height))
        self.red_img.convert()
        