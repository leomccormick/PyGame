import pygame
import os
from config import IMG_DIR, SND_DIR

BACKGROUND = 'background'
PLAYER = 'player'
ICE = 'ICE'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg')).convert()
    assets[PLAYER] = pygame.image.load(os.path.join(IMG_DIR, 'player.png')).convert()
    assets[ICE] = pygame.image.load(os.path.join(IMG_DIR, 'ICE.jpg')).convert()
    
    # Carrega os sons do jogo
    # pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    # pygame.mixer.music.set_volume(0.4)
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets
