import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Catastrophe')

game_exit = False

pygame.display.update()

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

pygame.quit()
quit()