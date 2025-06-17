import pygame, time, os, sys, random
pygame.mixer.init()


middleRect = pygame.Rect(175, 150, 1200, 600)
button1 = pygame.Rect(675, 275, 200, 75)
button2 = pygame.Rect(675, 375, 200, 75)

start = True
game =  False
game2 = False

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

clock = pygame.time.Clock()

screensize = (1920, 900)
screen = pygame.display.set_mode((screensize),pygame.FULLSCREEN)


os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

movementx = 2
movementy = 2
music = "Music.mp3"
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
DB = (8, 26, 65)

screensize = (1920, 900)

screen = pygame.display.set_mode((screensize),pygame.FULLSCREEN)
background1 = pygame.image.load("background.png").convert_alpha()
background1 = pygame.transform.scale(background1, screensize)


screenRect = screen.get_rect()

ballback = time.time()

orange = pygame.image.load("orange.png").convert_alpha()
orange = pygame.transform.scale(orange, (55, 55))

rectb = pygame.image.load("Tetris.png").convert_alpha()
rect2b = pygame.image.load("Tetris.png").convert_alpha()
rectb = pygame.transform.scale(rectb,(35,150))
rect2b = pygame.transform.scale(rect2b,(35,150))
orangeRect = orange.get_rect()


clock = pygame.time.Clock()

orangeRect.x, orangeRect.y = 400, 70


rect = pygame.Rect(100, 250, 35, 150)
rect2 = pygame.Rect(1400, 250, 35, 150)
dt = 0

hub = pygame.Rect(0, 0, 1920, 75)
#hubRect = hub.get_rect()


T_Pong = "Trinity-Pong"
    
    
punkte_p1 = 0
punkte_p2 = 0

font_large = pygame.font.SysFont("Noteworthy", 72)
font = pygame.font.SysFont("Noteworthy", 60)
font_small = pygame.font.SysFont(None, 50)
font_mega = pygame.font.SysFont("Noteworthy", 100)


playerScored = 0
showball = True
running = True
while running:
    if start:
        screen.fill(WHITE)

    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.draw.rect(screen, GREY, middleRect)
        pygame.draw.rect(screen, WHITE, button1)
        pygame.draw.rect(screen, WHITE, button2)
        
        
        main = font_small.render(T_Pong, False, DB)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                game = True
                start = False#
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button2.collidepoint(event.pos):
                game2 = True
                start = False
        
        screen.blit(main,(675, 290))
        

        pygame.display.flip()
    if game:
        dt = clock.tick(450) / 100
        t1 = "Player 1:  "+ str(punkte_p1)
        t2 = "Player 1:  "+ str(punkte_p2)
        player01 = font.render(t1, False, WHITE)
        player02 = font.render(t2, False, WHITE)
        screen.fill(DB)
        screen.blit(background1, (0, 0))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if showball:
            orangeRect.x += movementx
            orangeRect.y += movementy

        
        if orangeRect.y >= screensize[1]-90:
            movementy = movementy * -1

        if orangeRect.x >= screensize[0]-55:
            if showball:
                ballback = time.time()
            showball = False
            playerScored = 1


        if orangeRect.y <= 70:
            movementy = movementy *- 1

        if orangeRect.x <= 0:
            if showball:
                ballback = time.time()
            showball = False
            playerScored = 2
            


        pygame.draw.rect(screen, BLACK, rect)
        pygame.draw.rect(screen, BLACK, rect2)

        screen.blit(rectb,(100,rect.y))
        screen.blit(rect2b,(1400,rect2.y))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            rect.y -= 90 * dt
            screen.blit(rectb,(100,rect.y))
        if keys[pygame.K_s]:
            rect.y += 90 * dt

        if keys[pygame.K_UP]:
            rect2.y -= 90 * dt
        if keys[pygame.K_DOWN]:
            rect2.y += 90 * dt

        if orangeRect.colliderect(rect):
            movementx = movementx * -1
        
        if orangeRect.colliderect(rect2):
            movementx = movementx * -1
            

        if showball:
            screen.blit(orange, orangeRect)

        timeseconds = (time.time() - ballback)
        if not showball and timeseconds > 1:
            showball = True
            orangeRect.x = 700
            orangeRect.y = 70
            movementx = movementx * (-1)
            movementy = 2
            if playerScored == 1:
                punkte_p1 += 1
                playerScored = 0
            if playerScored == 2:
                punkte_p2 += 1
                playerScored = 0
                
                if punkte_p1 == 10:
                    running = False
                if punkte_p2 == 10:
                    running = False
        
        pygame.draw.rect(screen, GREY, hub)

        screen.blit(player01,(50, 30))
        screen.blit(player02,(1250, 30))

        pygame.display.flip()
        dt = clock.tick(600) / 100

    if game2:
        screensize = (600, 600)
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

        fruits = []  # globale Liste der Früchte, die gezeichnet werden

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
                        fruits = spawn_fruits()  # neue Früchte generieren
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
