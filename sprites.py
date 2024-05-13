from pygame.sprite import _Group
from config import *

class Player(pygame.sprite.Sprite):
        def __init__(self, groups, assets):
            pygame.sprite.Sprite.__init__(self)

            self.image = assets[PLAYER_IMG]
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

        self.image = assets[ICE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if lane == 0:
            self.rect.x = 125
        elif lane == 1:
            self.rect.x = 375
        elif lane == 2:
            self.rect.x = 600
        self.rect.y = 0
        self.speed = 50
        self.groups = groups
        self.assets = assets
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <= HEIGHT:
            self.kill()