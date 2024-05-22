import pygame
from assets import load_assets
from config import FPS, INIT, BG_QUIT, WIDTH, HEIGHT, WHITE, YELLOW
from os import path

def leaderboard_screen(window, score):
    def salvar_pontuacao(pontuacao, nome_jogador):
        with open('leaderboard.txt', 'a') as arquivo:
            arquivo.write(f"{nome_jogador}: {pontuacao}\n")

    def mostrar_leaderboard():
        with open('leaderboard.txt', 'r') as arquivo:
            leaderboard = []
            for linha in arquivo:
                nome, pontuacao = linha.strip().split(': ')
                leaderboard.append((nome, int(pontuacao)))
            leaderboard.sort(key=lambda x: x[1], reverse=True) # Ordena o leaderboard pela pontuação maior para menor
            top_10 = leaderboard[:10]
            lista_nomes = [f"{nome}: {pontuacao}" for nome, pontuacao in top_10]
            return lista_nomes

    def draw_text(text, font, color, surface, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    clock = pygame.time.Clock()
    assets = load_assets()
    font = pygame.font.Font(None, 36)
    nome_jogador = ""
    input_active = True  # Pro jogador digitar o nome

    running = True
    while running:
        clock.tick(FPS)

        window.fill((0, 0, 0))  # Preenche a tela com a cor preta
        
        if input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = None
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if input_active:
                            salvar_pontuacao(score, nome_jogador)
                            input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        nome_jogador = nome_jogador[:-1]
                    else:
                        nome_jogador += event.unicode
            draw_text("Digite seu nome:", font, WHITE, window, WIDTH // 2, HEIGHT // 4)
            draw_text(nome_jogador, font, WHITE, window, WIDTH // 2, HEIGHT // 2)
        else:
            leaderboard = mostrar_leaderboard()
            draw_text("Aperte qualquer tecla", font, YELLOW, window, WIDTH // 2, 50)
            draw_text("para jogar novamente", font, YELLOW, window, WIDTH // 2, 85)
            draw_text("Melhores pontuações:", font, WHITE, window, WIDTH // 2, HEIGHT // 4 - 30)
            for i, linha in enumerate(leaderboard):
                draw_text(linha, font, WHITE, window, WIDTH // 2, HEIGHT // 4 + 40 * (i+1))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = None
                    running = False
                if event.type == pygame.KEYDOWN:
                    state = INIT
                    running = False
 
        pygame.display.flip()

    return state
