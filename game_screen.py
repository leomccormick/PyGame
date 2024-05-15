from config import FPS, situations, IMG_DIR, BACKGROUND
from assets import load_assets
from sprites import Player, Ice
from os import path
import pygame
import random

def game_screen(window):
    clock = pygame.time.Clock()
    
    assets = load_assets()

    background = pygame.image.load(path.join(IMG_DIR, 'background.jpg')).convert()

    IceVelM = 1

    # Criando grupo de gelos
    all_sprites = pygame.sprite.Group()
    all_ice = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_ice'] = all_ice
    tempo = 0
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

        if len(all_ice.sprites()) == 0:
            issue = random.choice(situations)
            situacaoDuracao = 0

        if situacaoDuracao % 5 == 0:
            i = int(situacaoDuracao/5)
            for gelo in range(len(issue[i])):
                if issue[i][gelo] != -2:
                    IcE = Ice(groups, assets, gelo)
                    all_sprites.add(IcE)
                    all_ice.add(IcE)

        situacaoDuracao += 1/FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_ESCAPE:
                        state = DONE
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if player.parado and player.rect.x != 625:
                            player.speedx = 5
                            player.parado = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if player.parado and player.rect.x != 125:
                            player.speedx = 5
                            player.parado = False

        all_sprites.update()
        
        tempo += 1/FPS

        if tempo % 30 == 0:
            fase += 1
            IceVelM += 0.1

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_ice, False, pygame.sprite.collide_mask)
        if len(hits) > 0:
            now = pygame.time.get_ticks()
        
        window.blit(assets[BACKGROUND], (0, 0))
        all_sprites.draw(window)

        pygame.display.update()
    pygame.quit()