import pygame
from assets import load_assets
from config import FPS, INIT, WIDTH, HEIGHT, WHITE, YELLOW

def leaderboard_screen(window, score):
    # Função para salvar a pontuação do jogador
    def salvar_pontuacao(pontuacao, nome_jogador):
        with open('leaderboard.txt', 'a') as arquivo:
            arquivo.write(f"{nome_jogador}: {pontuacao}\n")

    # Função para mostrar o leaderboard na tela
    def mostrar_leaderboard():
        # Abre o arquivo do leaderboard
        with open('leaderboard.txt', 'r') as arquivo:
            leaderboard = []
            # Lê cada linha do arquivo e extrai o nome e a pontuação
            for linha in arquivo:
                nome, pontuacao = linha.strip().split(': ')
                leaderboard.append((nome, int(pontuacao)))
            # Ordena o leaderboard pela pontuação, do maior para o menor
            leaderboard.sort(key=lambda x: x[1], reverse=True)
            # Seleciona apenas os top 10 jogadores
            top_10 = leaderboard[:10]
            # Formata as informações para exibição na tela
            lista_nomes = [f"{nome}: {pontuacao}" for nome, pontuacao in top_10]
            return lista_nomes

    # Função para desenhar texto na tela
    def draw_text(text, font, color, surface, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    # Inicializa o relógio para controle de FPS
    clock = pygame.time.Clock()
    # Carrega os assets necessários
    assets = load_assets()
    # Define a fonte e o tamanho do texto
    font = pygame.font.Font(None, 36)
    # Variável para o nome do jogador
    nome_jogador = ""
    # Define a entrada de texto como ativa para permitir que o jogador digite seu nome
    input_active = True  

    # Variável para controlar a execução do loop principal
    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Preenche a tela com a cor preta
        window.fill((0, 0, 0))  

        # Verifica se a entrada de texto está ativa
        if input_active:
            # Processa os eventos (mouse, teclado, botão, etc.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = None
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if input_active:
                            # Salva a pontuação do jogador quando a tecla Enter é pressionada
                            salvar_pontuacao(score, nome_jogador)
                            input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        # Remove o último caractere do nome do jogador quando a tecla Backspace é pressionada
                        nome_jogador = nome_jogador[:-1]
                    else:
                        # Adiciona o caractere digitado ao nome do jogador
                        nome_jogador += event.unicode
            # Desenha o texto "Digite seu nome:"
            draw_text("Digite seu nome:", font, WHITE, window, WIDTH // 2, HEIGHT // 4)
            # Desenha o nome do jogador
            draw_text(nome_jogador, font, WHITE, window, WIDTH // 2, HEIGHT // 2)
        else:
            # Mostra o leaderboard na tela
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
                    # Retorna ao estado inicial do jogo quando qualquer tecla é pressionada
                    state = INIT
                    running = False
 
        # Atualiza a tela
        pygame.display.flip()

    return state