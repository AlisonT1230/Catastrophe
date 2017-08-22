from tangible import Tangible
import pygame
import os

class Ground(Tangible):

    def __init__(self, x, y, block_type):
        """
        Initializes a type ground block at (x, y).

        Keyword arguments:

        x -- x position
        y -- y position
        block_type -- a string specifying the type of ground block
        """
        super(Ground, self).__init__(x, y, 100, 100)
        self.type = block_type

        #   Load images

        self.wood_planks = pygame.image.load(os.path.join("../textures/blocks/" + block_type + ".bmp"))
        self.wood_planks = pygame.transform.scale(self.wood_planks, (self.width, self.height))
        self.wood_planks.convert()
        self.stone = pygame.image.load(os.path.join("../textures/blocks/" + block_type + ".bmp"))
        self.stone = pygame.transform.scale(self.stone, (self.width, self.height))
        self.stone.convert()
        