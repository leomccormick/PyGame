import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from game_screen import main
from init_screen import init_screen

pygame.init()
pygame.mixer.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avalanche")

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(WINDOW)
    elif state == GAME:
        state = main(WINDOW)
    else:
        state = QUIT

pygame.quit()