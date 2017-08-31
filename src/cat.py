import settings
import pygame
import os

from tangible import Tangible

TERMINAL_VELOCITY = 25

class Cat(Tangible):

    def __init__(self, x, y, col):
        super(Cat, self).__init__(x, y, 100, 100)
        self.dx, self.dy = 0, 0
        self.kneading = False
        self.ground_height = settings.screen_height - self.height

        #   Load all images

        self.i1 = pygame.image.load(os.path.join("../textures/cats/black_cat_i1.bmp"))
        self.i1 = pygame.transform.scale(self.i1, (self.width, self.height))
        self.i1.convert()

        self.i2 = pygame.image.load(os.path.join("../textures/cats/black_cat_i2.bmp"))
        self.i2 = pygame.transform.scale(self.i2, (self.width, self.height))
        self.i2.convert()

        self.w1 = pygame.image.load(os.path.join("../textures/cats/black_cat_w1.bmp"))
        self.w1 = pygame.transform.scale(self.w1, (self.width, self.height))
        self.w1.convert()

        self.w2 = pygame.image.load(os.path.join("../textures/cats/black_cat_w2.bmp"))
        self.w2 = pygame.transform.scale(self.w2, (self.width, self.height))
        self.w2.convert()

        self.k1 = pygame.image.load(os.path.join("../textures/cats/black_cat_k1.bmp"))
        self.k1 = pygame.transform.scale(self.k1, (self.width, self.height))
        self.k1.convert()

        self.k2 = pygame.image.load(os.path.join("../textures/cats/black_cat_k2.bmp"))
        self.k2 = pygame.transform.scale(self.k2, (self.width, self.height))
        self.k2.convert()

        self.img = self.i1       #   default image
        

    def update(self, count, boundary_x, boundary_y):
        self.__update_position(boundary_x, boundary_y)
        self.__update_img(count)


    def update_position(self, boundary_x, boundary_y):
        """Updates the position according to velocity and boundaries."""
        if self.dx > 0 and not self.kneading:
            if self.x < boundary_x - self.width:
                self.x += self.dx
            else:
                self.x = boundary_x - self.width
        elif self.dx < 0 and not self.kneading:
            if self.x > 0:
                self.x += self.dx
            else:
                self.x = 0
        if self.dy >= 0:
            if self.y < self.ground_height:
                self.y += self.dy
                self.dy += 1
            else:
                self.y = self.ground_height
                self.dy = 0
        elif self.dy < 0:
            if self.y > -boundary_y:
                self.y += self.dy
                self.dy += 1
            else:
                self.dy = 0
        if self.dy >= TERMINAL_VELOCITY:
            self.dy = TERMINAL_VELOCITY
    

    def update_blanket_val(self, blankets):
        for b in blankets:
            if self.is_collide(b) and self.y + self.height <  b.y + 50:
                self.on_blanket = True
                self.ground_height = b.y - self.height
                self.grounded = True
                break
            else:
                if self.grounded:
                    self.grounded = False
                    self.on_blanket = False
                    self.ground_height = settings.screen_height - self.height

    
    def update_ground_val(self, ground_blocks):
        for g in ground_blocks:
            if self.is_collide(g):
                if self.y + self.height < g.y + TERMINAL_VELOCITY:             #   cat bottom collided
                    self.y = g.y - self.height
                    self.ground_height = g.y - self.height
                    self.grounded = True
                    break
                elif self.y > g.y + g.height - 35:              #   cat top collided
                    self.y = g.y + g.height
                    self.dy = 0
                elif self.x + self.width < g.x + 35:            #   cat right collided
                    self.x = g.x - self.width
                elif self.x > g.x + g.width - 35:                    #   cat left collided
                    self.x = g.x + g.width
            else:
                if not self.grounded:
                    self.ground_height = settings.screen_height - self.height
                    self.grounded = False


    def update_img(self, count):
        """
        Updates the image to the correct animation 
        frame according to the count.
        """
        if self.kneading:
            if count < 26 or (count > 50 and count < 76):
                self.img = self.k1
            else:
                self.img = self.k2
        elif self.dx == 0:
            if count < 51:
                self.img = self.i1
            else:
                self.img = self.i2
        else:
            if count/10 == 0 or count/10 == 2 or count/10 == 4 or count/10 == 6 or count/10 == 8 or count/10 == 10 == 0:
                self.img = self.w1
            else:
                self.img = self.w2
