from config import *
from operacoes import *
from assets import *
from sprites import *

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

     # Carrega o fundo da tela inicial
    # background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert() 
    # background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False