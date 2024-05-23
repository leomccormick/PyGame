import pygame
import os
from config import WIDTH, HEIGHT, PEDRA, BG_QUIT, BG_INIT, IMG_DIR, SND_DIR, BACKGROUND, PLAYER, PLAYER_HEIGHT, PLAYER_WIDTH, ARVORE, ARVORE_WIDTH, ARVORE_HEIGHT, SCORE_FONT, FNT_DIR, NEVE, MUSIC

def load_assets():
    # Cria um dicionário para armazenar os recursos do jogo
    assets = {}

    # Carrega as imagens do diretório IMG_DIR e as dimensiona conforme necessário
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg'))
    assets[PLAYER] = pygame.image.load(os.path.join(IMG_DIR, 'player.png'))
    assets[PLAYER] = pygame.transform.scale(assets[PLAYER], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[ARVORE] = pygame.image.load(os.path.join(IMG_DIR, 'arvore.png'))
    assets[ARVORE] = pygame.transform.scale(assets[ARVORE], (ARVORE_WIDTH, ARVORE_HEIGHT))
    assets[PEDRA] = pygame.image.load(os.path.join(IMG_DIR, 'pedra.png'))
    assets[PEDRA] = pygame.transform.scale(assets[PEDRA], (ARVORE_WIDTH, ARVORE_HEIGHT))
    assets[BG_INIT] = pygame.image.load(os.path.join(IMG_DIR, 'CAPA_CORRIGIDA.png'))
    assets[BG_INIT] = pygame.transform.scale(assets[BG_INIT], (WIDTH, HEIGHT))
    assets[BG_QUIT] = pygame.image.load(os.path.join(IMG_DIR, 'gameover.png'))
    assets[BG_QUIT] = pygame.transform.scale(assets[BG_QUIT], (WIDTH+15, HEIGHT+15))

    # Carrega o som de neve do diretório SND_DIR
    assets[NEVE] = pygame.mixer.Sound(os.path.join(SND_DIR, 'Neve.mp3'))

    # Carrega a fonte da pontuação do diretório FNT_DIR
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    return assets
