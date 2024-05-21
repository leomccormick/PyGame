import pygame
import os
from config import BG_QUIT, BG_INIT, IMG_DIR, SND_DIR, BACKGROUND, PLAYER, ICE, PLAYER_HEIGHT, PLAYER_WIDTH, ICE_HEIGHT, ICE_WIDTH, ARVORE, ARVORE_WIDTH, ARVORE_HEIGHT, SCORE_FONT, FNT_DIR


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg'))
    assets[PLAYER] = pygame.image.load(os.path.join(IMG_DIR, 'player.png'))
    assets[PLAYER] = pygame.transform.scale(assets[PLAYER], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[ICE] = pygame.image.load(os.path.join(IMG_DIR, 'ICE.png'))
    assets[ICE] = pygame.transform.scale(assets[ICE], (ICE_WIDTH, ICE_HEIGHT))
    assets[ARVORE] = pygame.image.load(os.path.join(IMG_DIR, 'arvore.png'))
    assets[ARVORE] = pygame.transform.scale(assets[ARVORE], (ARVORE_WIDTH, ARVORE_HEIGHT))
    assets[BG_INIT] = pygame.image.load(os.path.join(IMG_DIR, 'CAPA.jpg'))
    assets[BG_QUIT] = pygame.image.load(os.path.join(IMG_DIR, 'gameover.jpeg'))

    # Carrega as fontes
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    # pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    # pygame.mixer.music.set_volume(0.4)
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets