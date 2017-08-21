from tangible import Tangible
import pygame
import os

class Ground(Tangible):

    def __init__(self, x, y):
        super(Ground, self).__init__(x, y, 100, 100)

        #   Load images

        self.wood_planks = pygame.image.load(os.path.join("textures/blocks/wood_planks.bmp"))
        self.wood_planks = pygame.transform.scale(self.wood_planks, (self.width, self.height))
        self.wood_planks.convert()
        