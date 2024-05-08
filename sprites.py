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