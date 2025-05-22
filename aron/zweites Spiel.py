import pygame, time, os, sys
pygame.mixer.init()

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

punkte_p1 = 0
punkte_p2 = 0

font_large = pygame.font.SysFont("Noteworthy", 72)
font = pygame.font.SysFont("Noteworthy", 60)
font_small = pygame.font.SysFont(None, 40)

player01 = font.render("Player 1 = ,", False, BLUE)
player02 = font.render("Player 2", False, BLUE)

showball = True
running = True
while running:
    screen.fill(WHITE)
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
        punkte_p1 = +1


    if orangeRect.y <= 70:
        movementy = movementy *- 1

    if orangeRect.x <= 0:
        if showball:
            ballback = time.time()
        showball = False 
        punkte_p2 = +1
        


    pygame.draw.rect(screen, BLACK, rect)
    pygame.draw.rect(screen, BLACK, rect2)

    screen.blit(rectb,(100,rect.y))
    screen.blit(rect2b,(1400,rect2.y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect.y -= 60 * dt
        screen.blit(rectb,(100,rect.y))
    if keys[pygame.K_s]:
        rect.y += 60 * dt

    if keys[pygame.K_UP]:
        rect2.y -= 60 * dt
    if keys[pygame.K_DOWN]:
        rect2.y += 60 * dt

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
    
    pygame.draw.rect(screen, GREY, hub)

    screen.blit(player01,(50, 30))
    screen.blit(player02,(1300, 30))

    pygame.display.flip()
    dt = clock.tick(300) / 100
