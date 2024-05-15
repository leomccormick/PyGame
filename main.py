import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avalanche")

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(WINDOW)
    elif state == GAME: 
        state = game_screen(WINDOW)
    else:
        state = QUIT

pygame.quit()