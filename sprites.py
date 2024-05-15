from pygame.sprite import Group
import pygame
from config import WIDTH, HEIGHT
from assets import load_assets, PLAYER, ICE

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
        self.acaeleracao = 0
        self.groups = groups
        self.assets = assets
        
    def update(self):
        self.rect.x += self.speedx
        self.speedx += self.acaeleracao
        if self.rect.x % (WIDTH/3) == 0:
            self.acaeleracao *= -1
        if self.rect.x % (WIDTH/3 - WIDTH/6) == 0:
            self.acaeleracao *= 0
            self.rect.x *= 0

class Ice(pygame.sprite.Sprite):
    def __init__(self, groups, assets, lane):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ICE]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if lane == 0:
            self.rect.x = 125
        elif lane == 1:
            self.rect.x = 375
        elif lane == 2:
            self.rect.x = 600
        self.rect.y = 0
        self.speed = IceVelInit*IceVelM
        self.groups = groups
        self.assets = assets
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <= HEIGHT:
            self.kill()
        self.speed = IceVelInit*IceVelM
        self.rect.x += self.speedx
        self.speedx += self.acaeleracao
        if self.rect.x % (WIDTH/3) == 0:
            self.acaeleracao *= -1
        if self.rect.x % (WIDTH/3 - WIDTH/6) == 0:
            self.acaeleracao *= 0
            self.rect.x *= 0
