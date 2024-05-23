import pygame
from os import path
from config import IMG_DIR, FPS, QUIT, GAME, BLACK, WHITE, BG_INIT
from assets import load_assets

def init_screen(window):
    clock = pygame.time.Clock()  # Ajusta a velocidade do jogo
    assets = load_assets()  # Carrega os recursos

    running = True
    while running:
        clock.tick(FPS)

        # Processa eventos (fechar janela, teclas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = None
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = GAME
                    running = False
                if event.key == pygame.K_ESCAPE:
                    state = None
                    running = False

        window.blit(assets[BG_INIT], (0, 0))  # Desenha o fundo
        pygame.display.flip()  # Atualiza o display

    return state
