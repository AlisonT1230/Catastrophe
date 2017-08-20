import settings
import pygame
import os

from tangible import Tangible

MAX_KNEAD = 100
MAX_HEALTH = 100
MAX_LIVES = 5

class Cat(Tangible):

    def __init__(self, x, y, col):
        super(Cat, self).__init__(x, y, 100, 100)
        self.dx, self.dy = 0, 0
        self.health = 100
        self.lives = 5
        self.knead_power = 0
        self.kneading = False
        self.on_blanket = False
        self.ground_height = settings.screen_height - self.height

        #   Load all images

        self.i1 = pygame.image.load(os.path.join("textures/cats/black_cat_i1.bmp"))
        self.i1 = pygame.transform.scale(self.i1, (self.width, self.height))
        self.i1.convert()

        self.i2 = pygame.image.load(os.path.join("textures/cats/black_cat_i2.bmp"))
        self.i2 = pygame.transform.scale(self.i2, (self.width, self.height))
        self.i2.convert()

        self.w1 = pygame.image.load(os.path.join("textures/cats/black_cat_w1.bmp"))
        self.w1 = pygame.transform.scale(self.w1, (self.width, self.height))
        self.w1.convert()

        self.w2 = pygame.image.load(os.path.join("textures/cats/black_cat_w2.bmp"))
        self.w2 = pygame.transform.scale(self.w2, (self.width, self.height))
        self.w2.convert()

        self.k1 = pygame.image.load(os.path.join("textures/cats/black_cat_k1.bmp"))
        self.k1 = pygame.transform.scale(self.k1, (self.width, self.height))
        self.k1.convert()

        self.k2 = pygame.image.load(os.path.join("textures/cats/black_cat_k2.bmp"))
        self.k2 = pygame.transform.scale(self.k2, (self.width, self.height))
        self.k2.convert()

        self.img = self.i1       #   default image


    def update(self, count):
        self.__update_position()
        self.__update_img(count)
        self.__update_knead_val()


    def move_left(self):
        self.dx = -10


    def move_right(self):
        self.dx = 10


    def stop(self):
        self.dx = 0


    def jump(self):
        if self.y == self.ground_height and not self.kneading:
            self.dy = -20


    def knead(self):
        if self.knead_power < MAX_KNEAD and self.y == self.ground_height and self.on_blanket:
            self.kneading = True
        

    def stop_knead(self):
        self.kneading = False


    def add_health(self, amt):
        if self.health + amt < MAX_HEALTH:
            self.health += amt
        else:
            self.health = MAX_HEALTH


    def drop_health(self, amt):
        if self.health - amt > 0:
            self.health -= amt
        else:
            self.health = 0
            self.drop_life()

    
    def add_life(self):
        if self.lives < MAX_LIVES:
            self.lives += 1


    def drop_life(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            pass
            #   GAME OVER


    def __update_position(self):
        """Updates the position according to velocity and boundaries."""
        if self.dx > 0 and not self.kneading:
            if self.x < settings.screen_width - self.width:
                self.x += self.dx
            else:
                self.x = settings.screen_width - self.width
        elif self.dx < 0 and not self.kneading:
            if self.x > 0:
                self.x += self.dx
            else:
                self.x = 0
        if self.dy > 0:
            if self.y < self.ground_height:
                self.y += self.dy
            else:
                self.y = self.ground_height
        elif self.dy < 0:
            if self.y > 0:
                self.y += self.dy
        self.dy += 1
    

    def update_blanket_val(self, blanket):
        if self.is_collide(blanket):
            self.on_blanket = True
            self.ground_height = blanket.y - self.height
        else:
            self.on_blanket = False
            self.ground_height = settings.screen_height - self.height


    def __update_knead_val(self):
        if self.kneading:
            if self.knead_power < MAX_KNEAD:
                self.knead_power += 0.5
            else:
                self.stop_knead()


    def __update_img(self, count):
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
