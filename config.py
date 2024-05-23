from os import path

# Constantes para os nomes dos assets
BACKGROUND = 'background'
PLAYER = 'player'
ARVORE = 'arvore'
PEDRA = 'pedra'
SCORE_FONT = 'score_font'
BG_INIT = 'CAPA_CORRIGIDA'
BG_QUIT = 'gameover'
NEVE = 'Neve'
MUSIC = 'Music'

# Tamanhos dos sprites
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
ARVORE_WIDTH = 250
ARVORE_HEIGHT = 250

# Define as pastas que contêm os arquivos de assets
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'som')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo e tela
WIDTH = 3 * 250  # Largura da tela
HEIGHT = 3 * 250  # Altura da tela
FPS = 60  # Frames por segundo

# Define algumas cores básicas
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

# Situações possíveis para a geração de cenários
    # Cada cenário é representado por uma lista de listas, onde 1 representa a presença de um obstáculo e 0 a ausência
    # Os obstáculos são distribuídos em três faixas verticais, representadas pelas sublistas internas
    # Exemplo: [[0, 0, 0], [0, 1, 0], ...]
    # Neste exemplo, a primeira linha é vazia, a segunda tem um obstáculo na faixa do meio, e assim por diante
    # Cada cenário representa uma variação de obstáculos para o jogador enfrentar e é escolhido aleatoriamente pelo código
    # A quantidade de cenários pode ser ajustada ou expandida conforme necessário
situations = [
    [
        [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
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
        [1, 1, 0],
        [0, 1, 0],
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 1],
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
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
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 1]
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
        [1, 0, 0]
    ],
    [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 0],
        [1, 0, 1],
        [0, 0, 1],
        [0, 1, 1]
    ],
    [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 0],
        [1, 1, 0]
    ],
    [
        [0, 0, 0],
        [1, 0, 1],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 0],
        [1, 0, 1]
    ],
    [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
        [1, 1, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 1]
    ],
    [
        [0, 0, 0],
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ],
    [
        [0, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 0],
        [1, 0, 1],
        [0, 0, 0],
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 1]
    ],
    [
        [0, 0, 0],
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [1, 0, 1]
    ],
    [
        [0, 0, 0],
        [1, 0, 1],
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 0],
        [0, 0, 1],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ]
]


