from config import *
from assets import load_assets
import pygame

def main():
    game = True

    assets = load_assets()

    state = GAME
    
    keys_down = {}

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                break
            if state == GAME:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        ...
                    if event.key == pygame.K_RIGHT:
                        ...
                    if event.key == pygame.K_a:
                        ...
                    if event.key == pygame.K_d:
                        ...

                

    pygame.quit()