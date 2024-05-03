import random, math, time, pygame

# Tela:

Heigth = 4 * 250
Length = 3 * 250

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