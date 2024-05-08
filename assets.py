import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

BACKGROUND = 'background'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.png')).convert()