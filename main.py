from operacoes import *

pygame.init()

game = True

while game:
    for event in pygame.event.EventType():
        if event == pygame.QUIT:
            game = False
        

pygame.quit()