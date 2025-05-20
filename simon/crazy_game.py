import pygame, time
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
zhal = randint(1,4)
pygame.init()

screensize = (1420, 720)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(screensize)

asset = pygame.image.load("mein_asset_v2.jpg").convert_alpha()
assetx, assety = 450, 100

asset2 = pygame.image.load("mein_asset_v2.jpg").convert_alpha()
asset2x, asset2y = 850, 100

asset3 = pygame.image.load("mein_asset_v2.jpg").convert_alpha()
asset3x, asset3y = 650, 100

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        print(event)

    assety += 1
    asset2y += 1
    asset3y += 1

    if assety >= screensize[1]-20:
        assety -= 720

    if asset2y >= screensize[1]-20:
        asset2y -= 720

    if asset3y >= screensize[1]-20:
        asset3y -= 720

    screen.fill(BLACK)
    screen.blit(asset, (assetx, assety))
    screen.blit(asset2, (asset2x, asset2y))
    screen.blit(asset3, (asset3x, asset3y))

    pygame.display.flip()

clock.tick(30)