import pygame, time
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

screensize = (1420, 720)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

fruits = []

number = 1

screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

# lädt die füchte
bild1 = pygame.image.load("strawberry.png") #Erdbeere
bild2 = pygame.image.load("lemon.png") #Kirsche
bild3 = pygame.image.load("plum.png") #Blaubeere
bild4 = pygame.image.load("banana.png") #Anannas
bild5 = pygame.image.load("watermelon.png") #Apfel
bild6 = pygame.image.load("coconut.png") #Kiwi 

scaled_bild1 = pygame.transform.scale(bild1, (70, 70))
scaled_bild2 = pygame.transform.scale(bild2, (70, 70))
scaled_bild3 = pygame.transform.scale(bild3, (70, 70))
scaled_bild4 = pygame.transform.scale(bild4, (70, 70))
scaled_bild5 = pygame.transform.scale(bild5, (70, 70))
scaled_bild6 = pygame.transform.scale(bild6, (70, 70))

# beispiels-koordinaten wo die frucht spawnen kann
spawn_orte = [
    (100,100), (100,200), (100,300),
    (200,100), (200,200), (200,300),
    (300,100), (300,200), (300,300)
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
                        furcht_die_spawnt = scaled_bild1
                    elif 9 <= zahl <= 18:
                        furcht_die_spawnt = scaled_bild2
                    elif 19 <= zahl <= 28:
                        furcht_die_spawnt = scaled_bild3
                    elif 29 <= zahl <= 34:
                        furcht_die_spawnt = scaled_bild4
                    elif 35 <= zahl <= 35:
                        furcht_die_spawnt = scaled_bild5
                    elif zahl == 36:
                        furcht_die_spawnt = scaled_bild6

                    # wählt aus, wo die Frucht spawnt
                    if spawn_orte:  # Nur wenn noch Orte übrig sind
                        ausgewählt = random.choice(spawn_orte)
                        spawn_orte.remove(ausgewählt)
                        fruits.append((furcht_die_spawnt, ausgewählt))

                    number += 1  # nicht vergessen, sonst Endlosschleife

                    if event.key == pygame.K_SPACE:
                        #stoppt nach 9 früchten
                        screen.fill(BLACK)
                        while number <= 9:
                        # wählt aus, welche Frucht spawnt
                            zahl = random.randint(0, 36)

                            if 0 <= zahl <= 8:
                                furcht_die_spawnt = scaled_bild1
                            elif 9 <= zahl <= 18:
                                furcht_die_spawnt = scaled_bild2
                            elif 19 <= zahl <= 28:
                                furcht_die_spawnt = scaled_bild3
                            elif 29 <= zahl <= 34:
                                furcht_die_spawnt = scaled_bild4
                            elif 35 <= zahl <= 35:
                                furcht_die_spawnt = scaled_bild5
                            elif zahl == 36:
                                furcht_die_spawnt = scaled_bild6

                            # wählt aus, wo die Frucht spawnt
                            if spawn_orte:  # Nur wenn noch Orte übrig sind
                                ausgewählt = random.choice(spawn_orte)
                                spawn_orte.remove(ausgewählt)
                                fruits.append((furcht_die_spawnt, ausgewählt))

                            number += 1  # nicht vergessen, sonst Endlosschleife

        screen.fill(BLACK)
        for fruit, position in fruits:
            screen.blit(fruit, position)
        pygame.display.flip()
        clock.tick(30)