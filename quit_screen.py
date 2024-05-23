import pygame
from config import INIT, FPS, BG_QUIT
from assets import load_assets
from leaderboard_screen import leaderboard_screen

def quit_screen(window, score):
    # Inicializa o relógio para controle de FPS
    clock = pygame.time.Clock()

    # Desativa a música de fundo
    pygame.mixer.music.set_volume(0.0)

    # Carrega os assets necessários
    assets = load_assets()

    # Define a variável de controle de execução do loop principal
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

            # Verifica se uma tecla foi pressionada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = None
                    running = False
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    # Chama a tela do leaderboard se Enter for pressionado
                    state = leaderboard_screen(window, score)
                    running = False
                if event.key == pygame.K_SPACE:
                    # Reinicia o jogo se a barra de espaço for pressionada
                    pygame.mixer.music.set_volume(0.1)
                    state = INIT
                    running = False
        
        # Desenha o fundo na tela
        window.blit(assets[BG_QUIT], (0, 0))
        # Atualiza a tela
        pygame.display.update()

    return state
