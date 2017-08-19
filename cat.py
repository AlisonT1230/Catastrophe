import settings
import pygame
import os

MAX_KNEAD = 100

class Cat:

    def __init__(self, x, y, col):
        self.x, self.y, self.dx, self.dy = x, y, 0, 0
        self.width, self.height = 100, 100
        self.knead_power = 0
        self.kneading = False

        #   Load all images

        self.i1 = pygame.image.load(os.path.join("textures/cats/black_cat_i1.bmp"))
        self.i1 = pygame.transform.scale(self.i1, (100,100))
        self.i1.convert()

        self.i2 = pygame.image.load(os.path.join("textures/cats/black_cat_i2.bmp"))
        self.i2 = pygame.transform.scale(self.i2, (100,100))
        self.i2.convert()

        self.w1 = pygame.image.load(os.path.join("textures/cats/black_cat_w1.bmp"))
        self.w1 = pygame.transform.scale(self.w1, (100,100))
        self.w1.convert()

        self.w2 = pygame.image.load(os.path.join("textures/cats/black_cat_w2.bmp"))
        self.w2 = pygame.transform.scale(self.w2, (100,100))
        self.w2.convert()

        self.k1 = pygame.image.load(os.path.join("textures/cats/black_cat_k1.bmp"))
        self.k1 = pygame.transform.scale(self.k1, (100,100))
        self.k1.convert()

        self.k2 = pygame.image.load(os.path.join("textures/cats/black_cat_k2.bmp"))
        self.k2 = pygame.transform.scale(self.k2, (100,100))
        self.k2.convert()

        self.img = self.i1       #   default image

    def update(self, count, cursor_x, cursor_y):
        self.__update_follow(cursor_x, cursor_y)
        self.__update_position()
        self.__update_img(count)

    def move_left(self):
        self.dx = -10

    def move_right(self):
        self.dx = 10

    def stop(self):
        self.dx = 0

    def jump(self):
        if self.y == settings.screen_height - self.height and not self.kneading:
            self.dy = -20

    def knead(self):
        if self.knead_power < MAX_KNEAD and self.y == settings.screen_height - self.height:
            self.knead_power += 1
            self.kneading = True
        
    def stop_knead(self):
        self.kneading = False

    def __update_position(self):
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
            if self.y < settings.screen_height - self.height:
                self.y += self.dy
            else:
                self.y = settings.screen_height - self.height
        elif self.dy < 0:
            if self.y > 0:
                self.y += self.dy
        self.dy += 1
    
    def __update_img(self, count):
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


    def __update_follow(self, cursor_x, cursor_y):
        if self.x < cursor_x - 100:
            self.move_right()
        elif self.x > cursor_x:
            self.move_left()
        else:
            self.stop()
            if self.y > cursor_y + 200:
                self.jump()
