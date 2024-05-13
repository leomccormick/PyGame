from os import path

BACKGROUND = 'background'
PLAYER = 'player'
ICE = 'ICE'

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
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

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

# Situações:

# Trem esquerda = -1
# Trem meio = 0
# Trem direita = 1
# Sem trem = 2

#situação 1 exemplo:
#   [
#        [-1, 2, 2],
#        [-1, 2, 2],
#        [0, 2, 1],
#        [2, 2, 1],
#        [2, 2, 0],
#        [2, 2, 0]
#   ]
#       ,█     ,
#       ,█     ,
#       ,██   █,
#       ,     █,
#       ,    ██,
#       ,    ██,

situations = [
    [
        [-1, 2, 2],
        [-1, 2, 2],
        [0, 2, 1],
        [2, 2, 1],
        [2, 2, 0],
        [2, 2, 0]
    ],
    [
        [0, -1, 2],
        [0, -1, 2],
        [-1, 1, 0],
        [-1, 1, 0],
        [2, 0, 0],
        [2, 0, 0]
    ],
    [
        [2, 0, 0],
        [2, 0, 2],
        [-1, 0, 1],
        [2, 0, 1],
        [2, 0, -1],
        [2, 0, 2]
    ],
    [
        [0, 1, 0],
        [0, -1, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 1, 0],
        [0, -1, 0]
    ],
    [
        [0, 2, 0],
        [0, -1, 2],
        [-1, 0, 1],
        [2, 0, 1],
        [2, 2, 2],
        [0, 0, 2]
    ]
]

