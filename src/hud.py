import pygame

HEALTH_POS = (25, 25)
KNEAD_POS = (25, 45)
HEALTH_BAR = (100, 35)
KNEAD_BAR = (100, 55)
HUD_COLOUR = (245, 65, 100)
BAR_THICKNESS = 10

class HUD:

    def __init__(self):
        self.health_bar_width = 150
        self.knead_bar_width = 150

        font = pygame.font.Font("../fonts/BalooBhaijaan-Regular.ttf", 20)
        self.health_txt = font.render("Health", True, HUD_COLOUR)
        self.knead_txt = font.render("Knead", True, HUD_COLOUR)
        self.health_rect = pygame.Rect(HEALTH_BAR, (self.health_bar_width, BAR_THICKNESS))
        self.knead_rect = pygame.Rect(KNEAD_BAR, (self.knead_bar_width, BAR_THICKNESS))

    def update(self, health, knead):
        self.health_rect.width = 150 * health // 100
        self.knead_rect.width = 150 * knead // 100

