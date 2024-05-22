import pygame
import os
from config import WIDTH, HEIGHT, PEDRA, BG_QUIT, BG_INIT, IMG_DIR, SND_DIR, BACKGROUND, PLAYER, PLAYER_HEIGHT, PLAYER_WIDTH, ARVORE, ARVORE_WIDTH, ARVORE_HEIGHT, SCORE_FONT, FNT_DIR, NEVE, MUSIC


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg'))
    assets[PLAYER] = pygame.image.load(os.path.join(IMG_DIR, 'player.png'))
    assets[PLAYER] = pygame.transform.scale(assets[PLAYER], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[ARVORE] = pygame.image.load(os.path.join(IMG_DIR, 'arvore.png'))
    assets[ARVORE] = pygame.transform.scale(assets[ARVORE], (ARVORE_WIDTH, ARVORE_HEIGHT))
    assets[PEDRA] = pygame.image.load(os.path.join(IMG_DIR, 'pedra.png'))
    assets[PEDRA] = pygame.transform.scale(assets[PEDRA], (ARVORE_WIDTH, ARVORE_HEIGHT))
    assets[BG_INIT] = pygame.image.load(os.path.join(IMG_DIR, 'CAPA_CORRIGIDA.jpg'))
    assets[BG_QUIT] = pygame.image.load(os.path.join(IMG_DIR, 'gameover.png'))
    assets[BG_QUIT] = pygame.transform.scale(assets[BG_QUIT], (WIDTH+15, HEIGHT+15))
    assets[NEVE] = pygame.mixer.Sound(os.path.join(SND_DIR, 'Neve.mp3'))

    # Carrega as fontes
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    #dimensiona as capas
    #BG_INIT_dimensionado = pygame.transform.scale(assets[BG_INIT], (250, 250))
    #BG_QUIT_dimensionado = pygame.transform.scale(assets[BG_QUIT], (250, 250))

    # Carrega os sons do jogo
    # pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    # pygame.mixer.music.set_volume(0.4)
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    # assets[...] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets