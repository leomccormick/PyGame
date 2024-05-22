from pygame.sprite import Group
import pygame
from random import choice
from config import WIDTH, HEIGHT
from assets import PLAYER, ARVORE, PEDRA

IceVelInit = 50

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

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
        if self.rect.x == 275 or self.rect.x == 275-250 or self.rect.x == 275+250:
            self.speedx *= 0
            self.parado = True
        if self.rect.x == 275 -1 or self.rect.x == 275-250-1 or self.rect.x == 275+250-1:
            self.rect.x += -29
        elif self.rect.x == 275 +1 or self.rect.x == 275-250+1 or self.rect.x == 275+250+1:
            self.rect.x += 29
        else:
            self.rect.x += self.speedx

class Arvore(pygame.sprite.Sprite):
    def __init__(self, groups, assets, lane, fase):
        pygame.sprite.Sprite.__init__(self)
        self.multiplicador = 1
        self.image = choice((assets[ARVORE], assets[PEDRA]))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if lane == 0:
            self.rect.x = 20
        elif lane == 1:
            self.rect.x = 270
        elif lane == 2:
            self.rect.x = 520
        self.rect.y = -250
        self.groups = groups
        self.assets = assets
        self.speed = 0.7 + 0.3*(fase+4)
    
    def update(self):
#        self.multiplicador = 0.7 + 0.3*fase
#        self.rect.y += int(self.speed*self.multiplicador)
        self.rect.y += self.speed
        if self.rect.y >= HEIGHT:
            self.kill()
