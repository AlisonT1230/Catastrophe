import pygame
import os
from cat import Cat

class NPC(Cat):

    def __init__(self, x, y, col):
        super(NPC, self).__init__(x, y, col)
