import pygame
from config import *
from game_screen import main

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avalanche")

if __name__ == "__main__":
    main()