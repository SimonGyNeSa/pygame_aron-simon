import pygame,time, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

movementx = 2
movementy = 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

screensize = (1420, 720)
screen = pygame.display.set_mode(screensize)

screenRect = screen.get_rect(0, 0, 1420, 720)
print(screenRect)

orange = pygame.image.load("orange.png").convert_alpha()
orange = pygame.transform.scale(orange, (55, 55))

clock = pygame.time.Clock()

orangex, orangey = 400, 0

rect = pygame.Rect(100, 250, 35, 150)
rect2 = pygame.Rect(1280, 250, 35, 150)
dt = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    orangex += movementx
    orangey += movementy


    
    if orangey >= screensize[1]-55:
       movementy = movementy * -1

    if orangex >= screensize[0]-55:
        movementx = movementx * -1

    if orangey <= 0:
        movementy = movementy *- 1

    if orangex <= 0:
        movementx = movementx * -1


    print(orangex, orangey)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect.y -= 60 * dt
    if keys[pygame.K_s]:
        rect.y += 60 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect2.y -= 60 * dt
    if keys[pygame.K_DOWN]:
        rect2.y += 60 * dt
        
    
    screen.fill(WHITE)
    screen.blit(orange, (orangex,orangey))
    pygame.draw.rect(screen, BLACK, rect)
    pygame.draw.rect(screen, BLACK, rect2)

    pygame.display.flip()
    dt = clock.tick(200) / 100