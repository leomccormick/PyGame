from config import *
import pygame

def main():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                break

    pygame.quit()