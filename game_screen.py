from config import FPS
from assets import load_assets
from sprites import Player
import pygame

def main():
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando grupo de gelos
    all_sprites = pygame.sprite.Group()
    all_ice = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_ice'] = all_ice

    # Criando o jogador
    player = Player(groups, assets)
    all_sprites.add(player)

    DONE = 0
    PLAYING = 1
    state = PLAYING
    
    keys_down = {}
    score = 0
    fase = 1

    while state != DONE:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if player.parado and player.x != 625:
                            player.aceleracao = -125*2/0.09
                            player.parado = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if player.parado and player.x != 125:
                            player.aceleracao = 125*2/0.09
                            player.parado = False

        all_sprites.update()
        
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_ice, False, pygame.sprite.collide_mask)
        if len(hits) > 0:
            now = pygame.time.get_ticks()
        pygame.display.update()
    pygame.quit()