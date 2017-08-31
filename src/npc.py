import pygame
import os
from cat import Cat

class NPC(Cat):

    def __init__(self, x, y, name):
        super(NPC, self).__init__(x, y, 100, 100)
        if name is 'Ifloo':
            __load_iflah()
        elif name is 'Wendo': #19x18
            self.width = 76
            self.height = 72
            __load_wendo()
        elif name is 'Nosila':
            __load_nosila()
    

    def __load_iflah():
        self.i1 = pygame.image.load(os.path.join("../textures/cats/purple_cat_i1.bmp"))
        self.i1 = pygame.transform.scale(self.i1, (self.width, self.height))
        self.i1.convert()

        self.i2 = pygame.image.load(os.path.join("../textures/cats/purple_cat_i2.bmp"))
        self.i2 = pygame.transform.scale(self.i2, (self.width, self.height))
        self.i2.convert()

    
    def __load_wendo():
        self.i1 = pygame.image.load(os.path.join("../textures/cats/beige_cat_i1.bmp"))
        self.i1 = pygame.transform.scale(self.i1, (self.width, self.height))
        self.i1.convert()

        self.i2 = pygame.image.load(os.path.join("../textures/cats/beige_cat_i2.bmp"))
        self.i2 = pygame.transform.scale(self.i2, (self.width, self.height))
        self.i2.convert()

    
    def __load_nosila():
        self.i1 = pygame.image.load(os.path.join("../textures/cats/red_cat_i1.bmp"))
        self.i1 = pygame.transform.scale(self.i1, (self.width, self.height))
        self.i1.convert()

        self.i2 = pygame.image.load(os.path.join("../textures/cats/red_cat_i2.bmp"))
        self.i2 = pygame.transform.scale(self.i2, (self.width, self.height))
        self.i2.convert()
