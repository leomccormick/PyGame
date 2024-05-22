from os import path

BACKGROUND = 'background'
PLAYER = 'player'
ARVORE = 'arvore'
SCORE_FONT = 'score_font'
BG_INIT = 'CAPA_CORRIGIDA'
BG_QUIT = 'gameover'
NEVE = 'Neve'
MUSIC = 'Music'
PEDRA = 'pedra'


# Tamanhos dos sprites
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
ARVORE_WIDTH = 250
ARVORE_HEIGHT = 250

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'som')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo e tela.
WIDTH = 3 * 250 # Largura da tela
HEIGHT = 3 * 250 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_YELLOW = (255, 200, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

# Situações:

situations = [
    [
        [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1],
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
        [1, 1, 0],
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ],
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1],
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0],
        [1, 0, 1]
    ],
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1]
    ],
    [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 1],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
        [1, 1, 0]
    ]
]

