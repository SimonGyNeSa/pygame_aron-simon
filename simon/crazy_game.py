# --HINWEIS: EINFACH LEERTASTE DRÜCKEN // EINMAL KOSTET 5 DOGECOIN-- #


# # --ALLGEMEINE BEFEHLE-- #
import pygame, random, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import time

pygame.init()

screensize = (600, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 130, 230)
DARK_BLUE = (30, 100, 200)
RED = (200, 50, 50)
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

# --MUSIK UND TEXT LADEN-- #
pygame.mixer.music.load("standart_musik.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)
font = pygame.font.SysFont('Comic Sans MS', 40, bold=True)
kleiner_font = pygame.font.SysFont('Comic Sans MS', 30, bold=True)
pleite = pygame.mixer.Sound("sad-ending.wav")
effect = pygame.mixer.Sound("effect2.wav")
effect3 = pygame.mixer.Sound("effect3.wav")


# --LISTEN UND VARIABELN DEFENIEREN // BILDER LADEN-- #
fruits = []
dogecoin = 69
counter = 0
rechteck = pygame.Rect(150, 150, 295, 295)
variabel = 0
letzter_spin_zeit = 0  # Zeitpunkt des letzten Spins

spawn_orte = [
    (160, 160), (260, 160), (360, 160),
    (160, 260), (260, 260), (360, 260),
    (160, 360), (260, 360), (360, 360)
]

new_cursor = pygame.image.load("pointer_c_shaded.png")

ct = 0
indic = 3
gamblecount = 0
x2 = False
counterx2 = 0
einsatz = 5
multi = 1
bild1 = pygame.image.load("strawberry.png")
bild2 = pygame.image.load("lemon.png")
bild3 = pygame.image.load("plum.png")
bild4 = pygame.image.load("banana.png")
bild5 = pygame.image.load("watermelon.png")
bild6 = pygame.image.load("coconut.png")
hintergrund = pygame.image.load("hintergrund.webp")


scaled_bild1 = pygame.transform.scale(bild1, (70, 70))
scaled_bild2 = pygame.transform.scale(bild2, (70, 70))
scaled_bild3 = pygame.transform.scale(bild3, (70, 70))
scaled_bild4 = pygame.transform.scale(bild4, (70, 70))
scaled_bild5 = pygame.transform.scale(bild5, (70, 70))
scaled_bild6 = pygame.transform.scale(bild6, (70, 70))
hintergrund = pygame.transform.scale(hintergrund, (900, 600))


gewinn2 = pygame.image.load("2.png")
gewinn6 = pygame.image.load("6.png")
gewinn15 = pygame.image.load("15.png")
gewinn25 = pygame.image.load("25.png")
gewinn50 = pygame.image.load("50.png")
gewinn250 = pygame.image.load("250.png")



a = False
b = False
c = False
d = False
e = False

ac = 0
bc = 0
cc = 0
dc = 0
ec = 0

scaled_gewinn2 = pygame.transform.scale(gewinn2, (129, 70))
scaled_gewinn6 = pygame.transform.scale(gewinn6, (129, 70))
scaled_gewinn15 = pygame.transform.scale(gewinn15, (129, 70))
scaled_gewinn25 = pygame.transform.scale(gewinn25, (129, 70))
scaled_gewinn50 = pygame.transform.scale(gewinn50, (129, 70))
scaled_gewinn250 = pygame.transform.scale(gewinn250, (129, 70))

# --9x FRÜCHTE UND DEREN SPAWNORTE AUSWÄHLEN-- #
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

# --FÜGT BUTTONS HINZU-- #
class Button:
    def __init__(self, text, x, y, width, height, bg_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.rect, width=2, border_radius=10)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

button_autoplay = Button("Autoplay", 50, 500, 210, 65, BLUE, WHITE)
button_2x = Button("2x", 300, 500, 210, 65, RED, WHITE)

# --FUNKTION DES PROGRAMMS // BETÄTIGEN WENN LEERTASTE GEDRÜCKT // GEWINN AUSCHÜTTEN // CHECKEN OB SPIELER PLEITE IST-- #
running = True
while running:
    screen.fill(WHITE)
    screen.blit(hintergrund,(-200,0))
    cursor = pygame.cursors.Cursor((0,0), new_cursor)
    pygame.mouse.set_cursor(cursor)
    pygame.draw.rect(screen, BLACK, rechteck, 4, border_radius=10)

    button_autoplay.draw(screen)
    button_2x.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if button_autoplay.is_clicked(event.pos):
                print("Autoplay gedrückt")
            if button_2x.is_clicked(event.pos):
                print("lingangu")
                counterx2 = 0
                x2 = True
                einsatz = 10
                multi = 2

            
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aktuelle_zeit = time.time()
                counterx2 += 1
                if aktuelle_zeit - letzter_spin_zeit >= 1.00:
                    letzter_spin_zeit = aktuelle_zeit
                    dogecoin -= einsatz
                    fruits, f1, f2, f3, f4, f5, f6 = spawn_fruits()

                    if f1 == 3 or f2 == 3 or f3 == 3 or f4 == 3 or f5 == 3 or f6 == 3:
                        dogecoin += 2*multi
                        variabel = 1
                        
                        a = True

                    if f1 == 9 or f2 == 9 or f3 == 9 or f4 == 9 or f5 == 9 or f6 == 4:
                        dogecoin += 6*multi

                        b = True

                    if f1 == 6 or f2 == 6 or f3 == 6 or f4 == 6 or f5 == 6 or f6 == 6:
                        dogecoin += 15*multi

                        effect.set_volume(0.25)
                        effect.play()
                        c = True

                    if f1 == 8 or f2 == 8 or f3 == 8 or f4 == 8 or f5 == 8 or f6 == 8:
                        dogecoin += 50*multi

                        effect3.set_volume(0.25)
                        effect.play()
                        d = True

                    if f1 == 9 or f2 == 9 or f3 == 9 or f4 == 9 or f5 == 9 or f6 == 9:
                        dogecoin += 250**multi

                        e = True
                    
    if a and ac < indic:
        ac += 1
        screen.blit(scaled_gewinn2, (390, 50))
    if ac >= indic:
        a = False
        ac = 0
    
    if b and bc < indic:
        bc += 1
        screen.blit(scaled_gewinn6, (390, 50))
    if bc >= indic:
        b = False
        bc = 0
    
    if c and cc < indic:
        cc += 1
        screen.blit(scaled_gewinn15, (390, 50))
    if cc >= indic:
        c = False
        cc = 0
    
    if d and ac < indic:
        dc += 1
        screen.blit(scaled_gewinn50, (390, 50))
    if dc >= indic:
        d = False
        dc = 0

    if e and ac < indic:
        ec += 1
        screen.blit(scaled_gewinn250, (390, 50))
    if ec >= indic:
        e = False
        ec = 0
    if x2 == True:
        x2font = font.render("x2",True,BLACK)
        screen.blit(x2font,(screensize[0]-50,50))

    if counterx2 >= 5:
        counterx2 = 0
        x2 = False
        multi = 1
        einsatz = 5


    for fruit, pos in fruits:
        screen.blit(fruit, pos)
 
    if dogecoin >= 0:
        text_surface = font.render(f"DOGECOIN: {dogecoin}", True, (BLACK))
        screen.blit(text_surface, (50, 50))
    
    if dogecoin <= 0:
        link_text = "Alle Dogecoin verzockt"
        texttext = kleiner_font.render(link_text, True, (BLACK))
        screen.fill(WHITE)
        screen.blit(texttext, (40, 160))
        link_text = "https://gluecksspielsucht-nrw.de/"
        texttext = kleiner_font.render(link_text, True, (BLACK))
        screen.blit(texttext, (40, 300))
        pygame.mixer.music.set_volume(0.0)
        pleite.set_volume(0.1)
        pleite.play()
        
    pygame.display.flip()
    clock.tick(3)

pygame.quit()
