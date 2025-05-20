import pygame, time
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

screensize = (1420, 720)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

number = 0

screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

# lädt die füchte
bild1 = pygame.image.load("pic1.png") #Erdbeere
bild2 = pygame.image.load("pic2.png") #Kirsche
bild3 = pygame.image.load("pic3.png") #Blaubeere
bild4 = pygame.image.load("pic4.png") #Anannas
bild5 = pygame.image.load("pic5.png") #Apfel
bild6 = pygame.image.load("pic6.png") #Kiwi 

# beispiels-koordinaten wo die frucht spawnen kann
spawn_orte = [
    (10,10), (10,20), (10,30)
    (20,10), (20,20), (20,30)
    (30,10), (30,20), (30,30)
]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        print(event)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
            #stoppt nach 9 früchten
                while number <= 9:
                # wählt aus, welche Frucht spawnt
                    zahl = random.randint(0, 36)

                    if 0 <= zahl <= 8:
                        furcht_die_spawnt = bild1
                    elif 9 <= zahl <= 18:
                        furcht_die_spawnt = bild2
                    elif 19 <= zahl <= 28:
                        furcht_die_spawnt = bild3
                    elif 29 <= zahl <= 34:
                        furcht_die_spawnt = bild4
                    elif 35 <= zahl <= 35:
                        furcht_die_spawnt = bild5
                    elif zahl == 36:
                        furcht_die_spawnt = bild6

                    # wählt aus, wo die Frucht spawnt
                    if spawn_orte:  # Nur wenn noch Orte übrig sind
                        ausgewählt = random.choice(spawn_orte)
                        spawn_orte.remove(ausgewählt)
                        screen.blit(furcht_die_spawnt, ausgewählt)

                    number += 1  # nicht vergessen, sonst Endlosschleife


    screen.fill(BLACK)
    pygame.display.flip()

clock.tick(30)