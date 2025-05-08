import pygame, time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

screensize = (1420, 720)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(screensize)


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        print(event)

    screen.fill(BLACK)

    rect = pygame.Rect(350, 300, 750, 350)
    pygame.draw.rect(screen, WHITE, rect, 6, 1)

    pygame.draw.line(screen, WHITE, (200, 100), (200, 500), 5)


    pygame.display.flip()

clock.tick(30)