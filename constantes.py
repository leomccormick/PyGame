from config import *

# Tela:

HEIGHT = 4 * 250
WIDTH = 3 * 250

# Imagens:



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
    ] 
]