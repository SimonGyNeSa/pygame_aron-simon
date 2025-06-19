import pygame, random, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import time

pygame.init()
screensize = (600, 600)
BLACK = (0, 0, 0)

pygame.mixer.music.load("standart_musik.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)

font = pygame.font.SysFont(None, 48)
pleite = pygame.mixer.Sound("sad-ending.wav")
effect = pygame.mixer.Sound("effect2.wav")
effect3 = pygame.mixer.Sound("effect3.wav")
dogecoin = 250

spawn_orte = [
    (160, 150), (260, 150), (360, 150),
    (160, 250), (260, 250), (360, 250),
    (160, 350), (260, 350), (360, 350)
]


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

fruits = []

def spawn_fruits():
    local_spawn_orte = spawn_orte.copy()
    fruits_local = []
    number = 0


    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0 
    f5 = 0
    f6 = 0

    while number < 9 and local_spawn_orte:
        zahl = random.randint(0, 36)

        if 0 <= zahl <= 8: 
            furcht_die_spawnt = scaled_bild1
            f6 += 1
        elif 9 <= zahl <= 18:
            furcht_die_spawnt = scaled_bild2
            f5 += 1
        elif 19 <= zahl <= 28:
            furcht_die_spawnt = scaled_bild3
            f4 += 1
        elif 29 <= zahl <= 34:
            furcht_die_spawnt = scaled_bild4
            f3 += 1
        elif 35 <= zahl <= 35:
            furcht_die_spawnt = scaled_bild5
            f2 += 1
        elif zahl == 36:
            furcht_die_spawnt = scaled_bild6
            f1 += 1
        
        ausgewählt = random.choice(local_spawn_orte)
        local_spawn_orte.remove(ausgewählt)
        fruits_local.append((furcht_die_spawnt, ausgewählt))
        number += 1

    return fruits_local, f1, f2, f3, f4, f5, f6

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dogecoin -= 5
                fruits, f1, f2, f3, f4, f5, f6 = spawn_fruits()

                if f1 == 3 or f2 == 3 or f3 == 3 or f4 == 3 or f5 == 3 or f6 == 3:
                    dogecoin += 2
                    text_surface = font.render("+2", True, (255, 255, 255))
                    screen.blit(text_surface, (400, 50))
                    

                if f1 == 9 or f2 == 9 or f3 == 9 or f4 == 9 or f5 == 9 or f6 == 4:
                    dogecoin += 6
                    text_surface = font.render("+6", True, (255, 255, 255))
                    screen.blit(text_surface, (400, 50))
                    effect.set_volume(0.5)
                    effect.play()

                if f1 == 6 or f2 == 6 or f3 == 6 or f4 == 6 or f5 == 6 or f6 == 6:
                    dogecoin += 15
                    text_surface = font.render("+15", True, (255, 255, 255))
                    screen.blit(text_surface, (400, 50))
                    effect.set_volume(0.5)
                    effect.play()

                if f1 == 8 or f2 == 8 or f3 == 8 or f4 == 8 or f5 == 8 or f6 == 8:
                    dogecoin += 50
                    text_surface = font.render("+50", True, (255, 255, 255))
                    screen.blit(text_surface, (400, 50))
                    effect.set_volume(0.5)
                    effect.play()

                if f1 == 9 or f2 == 9 or f3 == 9 or f4 == 9 or f5 == 9 or f6 == 9:
                    text_surface = font.render("+250", True, (255, 255, 255))
                    screen.blit(text_surface, (400, 50))
                
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
        screen.blit(texttext, (50, 300))
        pygame.mixer.music.set_volume(0.0)
        pleite.set_volume(0.1)
        pleite.play()
        
    pygame.display.flip()
    clock.tick(8)

pygame.quit()
