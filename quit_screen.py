import pygame
from os import path
import sys
from config import arquivo_pontuacoes, INIT, GAME, QUIT, FPS, WHITE, SCORE_FONT, WIDTH, HEIGHT, DARK_YELLOW, BG_QUIT
from assets import load_assets

font = pygame.font.Font(None, 36)
nome_jogador = ""
input_active = False
fim_de_jogo = False

# Caminho do arquivo onde as pontuações serão armazenadas

def quit_screen(window, score):

    def salvar_pontuacao(pontuacao, nome_jogador):
        with open('leaderboard.txt', 'a') as arquivo:
            arquivo.write(f"{nome_jogador}: {pontuacao}\n")

    def mostrar_leaderboard():
        try:
            with open('leaderboard.txt', 'r') as arquivo:
                print("Leaderboard:")
                for linha in arquivo:
                    print(linha.strip())
        except FileNotFoundError:
            print("Ainda não há pontuações registradas.")

    # nome_jogador = input("Digite o nome do jogador: ")
    # salvar_pontuacao(score, nome_jogador)
    # mostrar_leaderboard()

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