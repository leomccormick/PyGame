import pygame
from os import path
from config import INIT, FPS, BG_QUIT
from assets import load_assets
from leaderboard_screen import leaderboard_screen

def quit_screen(window, score):
    clock = pygame.time.Clock()

    pygame.mixer.music.set_volume(0.0)

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
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    state = leaderboard_screen(window, score)
                    running = False
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.set_volume(0.1)
                    state = INIT
                    running = False
        
        window.blit(assets[BG_QUIT], (0, 0))
        pygame.display.update()

    return state