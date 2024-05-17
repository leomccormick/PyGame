from config import FPS, situations, IMG_DIR, BACKGROUND, ARVORE_HEIGHT
from assets import load_assets
from sprites import Player, Arvore
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

    issue = [0, 0]
    situacaoDuracao = 100

    speed_screen = 5

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
                    arvore = Ice(groups, assets, i)
                    all_sprites.add(arvore)
                    all_ice.add(arvore)
            cenario.pop(0)
            if len(cenario) <= 3:
                cenario += random.choice(situations)

<<<<<<< HEAD
        for ice in all_ice:
            ice.speed = speed_screen
=======
        if situacaoDuracao % 50 == 0:
            i = int(situacaoDuracao/50)
            for tree in range(len(issue[i])):
                if issue[i][tree] != 0:
                    ArvorE = Arvore(groups, assets, tree)
                    all_sprites.add(ArvorE)
                    all_arvores.add(ArvorE)
>>>>>>> af1cdd81bb9b432732f02bbfeab1a4b21c002124

        situacaoDuracao += 1

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

        print(fase)

        if tempo % (30*60) == 0:
            fase += 1
        
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_arvores, False, pygame.sprite.collide_mask)
        if len(hits) > 0:
            now = pygame.time.get_ticks()
            state = DONE
        
        window.blit(assets[BACKGROUND], (0, 0))
        all_sprites.draw(window)

        pygame.display.update()
    pygame.quit()