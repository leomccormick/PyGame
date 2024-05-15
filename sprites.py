from pygame.sprite import Group
import pygame
from config import WIDTH, HEIGHT
from assets import load_assets, PLAYER, ICE, ARVORE

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
            self.rect.x += -9
        elif self.rect.x == 275 +1 or self.rect.x == 275-250+1 or self.rect.x == 275+250+1:
            self.rect.x += 9
        else:
            self.rect.x += self.speedx

class Ice(pygame.sprite.Sprite):
    def __init__(self, groups, assets, lane):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ARVORE]
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
        self.speed = 5
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= HEIGHT:
            self.kill()
