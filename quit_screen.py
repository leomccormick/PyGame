import pygame
from os import path
from config import INIT, GAME, QUIT, FPS, WHITE, SCORE_FONT, WIDTH, HEIGHT, DARK_YELLOW, BG_QUIT
from assets import load_assets

def quit_screen(window):
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
                if event.key == pygame.K_ESCAPE:
                    state = None
                    running = False
                if event.key == pygame.K_SPACE:
                    state = INIT
                    running = False
        
        window.blit(assets[BG_QUIT], (0, 0))
        pygame.display.update()

    return state