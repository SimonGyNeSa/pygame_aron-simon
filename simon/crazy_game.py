import pygame, random, os, time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screensize = (600, 600)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 48)

dogecoin = 250

spawn_orte = [
    (160, 150), (260, 150), (360, 150),
    (160, 250), (260, 250), (360, 250),
    (160, 350), (260, 350), (360, 350)
]

# Früchte laden und skalieren
bild1 = pygame.image.load("strawberry.png")
bild2 = pygame.image.load("lemon.png")
bild3 = pygame.image.load("plum.png")
bild4 = pygame.image.load("banana.png")
bild5 = pygame.image.load("watermelon.png")
bild6 = pygame.image.load("coconut.png")

scaled_bild1 = pygame.transform.scale(bild1, (70, 70))
scaled_bild2 = pygame.transform.scale(bild2, (70, 70))
scaled_bild3 = pygame.transform.scale(bild3, (70, 70))
scaled_bild4 = pygame.transform.scale(bild4, (70, 70))
scaled_bild5 = pygame.transform.scale(bild5, (70, 70))
scaled_bild6 = pygame.transform.scale(bild6, (70, 70))

screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

fruits = []  # globale Liste der Früchte, die gezeichnet werden

def spawn_fruits():
    local_spawn_orte = spawn_orte.copy()
    fruits_local = []
    number = 0

    while number < 9 and local_spawn_orte:
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
        
        ausgewählt = random.choice(local_spawn_orte)
        local_spawn_orte.remove(ausgewählt)
        fruits_local.append((furcht_die_spawnt, ausgewählt))
        number += 1

    return fruits_local

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fruits = spawn_fruits()  # neue Früchte generieren
                dogecoin -= 5

    # Früchte zeichnen
    for fruit, pos in fruits:
        screen.blit(fruit, pos)
        if dogecoin >= 0:
            text_surface = font.render(f"DOGECOIN: {dogecoin}", True, (255, 255, 255))
            screen.blit(text_surface, (50, 50))
    
    if dogecoin <= 0:
        link_text = "Alle Dogecoin verzockt"
        texttext = font.render(link_text, True, (255, 255, 255))
        screen.fill(BLACK)
        screen.blit(texttext, (50, 160))
        link_text = "https://gluecksspielsucht-nrw.de/"
        texttext = font.render(link_text, True, (255, 255, 255))
        screen.blit(texttext, (50, 260))

        #hier ist ein kleiner cheat eingbaut

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

import pygame
