import pygame
from random import choice
from config import WIDTH, HEIGHT
from assets import PLAYER, ARVORE, PEDRA

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        # Carrega a imagem do jogador e cria sua máscara de colisão
        self.image = assets[PLAYER]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.bottom = HEIGHT - 25
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.parado = True
        
    def update(self):
        # Verifica se o jogador está parado
        if self.rect.x == 275 or self.rect.x == 275 - 250 or self.rect.x == 275 + 250:
            self.speedx *= 0
            self.parado = True
        
        # Move o jogador para a esquerda ou direita
        if self.rect.x == 275 - 1 or self.rect.x == 275 - 250 - 1 or self.rect.x == 275 + 250 - 1:
            self.rect.x += -29
        elif self.rect.x == 275 + 1 or self.rect.x == 275 - 250 + 1 or self.rect.x == 275 + 250 + 1:
            self.rect.x += 29
        else:
            self.rect.x += self.speedx

class Arvore(pygame.sprite.Sprite):
    def __init__(self, groups, assets, lane, fase):
        pygame.sprite.Sprite.__init__(self)

        # Escolhe aleatoriamente entre uma árvore e uma pedra para gerar a imagem
        self.image = choice((assets[ARVORE], assets[PEDRA]))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        # Define a posição inicial da árvore com base na pista
        if lane == 0:
            self.rect.x = 20
        elif lane == 1:
            self.rect.x = 270
        elif lane == 2:
            self.rect.x = 520
        self.rect.y = -250
        self.groups = groups
        self.assets = assets
        
        # Define a velocidade da árvore com base na fase do jogo
        self.speed = 0.7 + 0.3 * (fase + 4)
    
    def update(self):
        # Atualiza a posição da árvore
        self.rect.y += self.speed
        
        # Remove a árvore quando ela sai da tela
        if self.rect.y >= HEIGHT:
            self.kill()
