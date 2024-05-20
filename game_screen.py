from config import QUIT, FPS, situations, IMG_DIR, BACKGROUND, ARVORE_HEIGHT, DARK_YELLOW, WIDTH, SCORE_FONT
from assets import load_assets
from sprites import Player, Arvore
from os import path
import pygame
import random

def game_screen(window):
    clock = pygame.time.Clock()
    
    assets = load_assets()

    background = assets[BACKGROUND]
    background_rect = background.get_rect()

    window.blit(background, background_rect)

    # Criando grupo de gelos
    all_sprites = pygame.sprite.Group()
    all_arvores = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_arvores'] = all_arvores
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

    speed_screen = 0.7 + 0.3*(fase+4)

    cenario = random.choice(situations)
    contador = 0

    while state != DONE:
        clock.tick(FPS)

        speed_screen = 0.7 + 0.3*(fase+4)
        contador += speed_screen
        if contador >= ARVORE_HEIGHT:
            contador = 0
            for i in range(3):
                if cenario[0][i] != 0:
                    arvore = Arvore(groups, assets, i, fase)
                    all_sprites.add(arvore)
                    all_arvores.add(arvore)
            cenario.remove(cenario[0])
            if len(cenario) <= 3:
                cenario += situations[random.randint(0, len(situations)-1)]

        for arvore in all_arvores:
            arvore.speed = speed_screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_ESCAPE:
                        state = DONE
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if player.parado and player.rect.x != 25:
                            player.rect.x -= 1
                            player.speedx = -15
                            player.parado = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if player.parado and player.rect.x != 525:
                            player.rect.x += 1
                            player.speedx = 15
                            player.parado = False

        all_sprites.update()

        tempo += 1
        if tempo % 6 == 0:
            score += 1*fase

        print(fase)
        print(score)

        if tempo % (5*60) == 0:
            fase += 1
        
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_arvores, False, pygame.sprite.collide_mask)
        if len(hits) > 0:
            now = pygame.time.get_ticks()
            state = DONE
        
        window.blit(assets[BACKGROUND], (0, 0))
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{}".format(score), True, DARK_YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        pygame.display.update()
    return QUIT