import pygame
from os import path
from config import IMG_DIR, FPS, QUIT, GAME, BLACK, WHITE, BG_INIT
from assets import load_assets


def init_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
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
                

        # A cada loop, redesenha o fundo e os sprites
        window.blit(assets[BG_INIT], (0, 0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state