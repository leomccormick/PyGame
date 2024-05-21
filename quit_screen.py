import pygame
from assets import load_assets
from config import FPS, INIT, BG_QUIT, WIDTH, HEIGHT
from os import path

def quit_screen(window, score):
    def salvar_pontuacao(pontuacao, nome_jogador):
        with open('leaderboard.txt', 'a') as arquivo:
            arquivo.write(f"{nome_jogador}: {pontuacao}\n")

    def mostrar_leaderboard():
        try:
            with open('leaderboard.txt', 'r') as arquivo:
                leaderboard = arquivo.readlines()
                return [linha.strip() for linha in leaderboard]
        except FileNotFoundError:
            return ["Ainda não há pontuações registradas."]

    def draw_text(text, font, color, surface, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    clock = pygame.time.Clock()
    assets = load_assets()
    font = pygame.font.Font(None, 36)
    nome_jogador = ""
    input_active = True  # Definindo como True para permitir que o jogador digite seu nome

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = None
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_active:
                        salvar_pontuacao(score, nome_jogador)
                        state = INIT
                elif event.key == pygame.K_BACKSPACE:
                    nome_jogador = nome_jogador[:-1]
                else:
                    nome_jogador += event.unicode

        window.fill((0, 0, 0))  # Preenche a tela com a cor preta
        # window.blit(assets[BG_QUIT], (0, 0))

        if input_active:
            draw_text("Digite seu nome:", font, (255, 255, 255), window, WIDTH // 2, HEIGHT // 4)
            draw_text(nome_jogador, font, (255, 255, 255), window, WIDTH // 2, HEIGHT // 2)
        else:
            leaderboard = mostrar_leaderboard()
            draw_text("Leaderboard:", font, (255, 255, 255), window, WIDTH // 2, HEIGHT // 4)
            for i, linha in enumerate(leaderboard):
                draw_text(linha, font, (255, 255, 255), window, WIDTH // 2, HEIGHT // 4 + 40 * (i+1))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = None
                        running = False

        print(nome_jogador)
        pygame.display.flip()

    return state
