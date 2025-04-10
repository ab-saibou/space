import pygame               # Pygame-Bibliothek importieren
import sys                  # Für sys.exit()

pygame.init()               # Pygame initialisieren
#def addBullet()
# Fenstergröße definieren
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))      # Fenster erstellen
pygame.display.set_caption("Mini Space Invader")    # Fenstertitel setzen

# Farben definieren
RED = (255, 0, 0)           # Rot für das Spieler-Quadrat
BLACK = (0, 0, 0)           # Schwarz für den Hintergrund
BCOLOR = (100,255,200)
# Spieler-Eigenschaften (rotes Quadrat)
player_width = 40           # Breite des Spielers
player_height = 20          # Höhe des Spielers
player_x = WIDTH // 2 - player_width // 2           # Startposition (zentriert)
player_y = HEIGHT - player_height - 30              # Etwas über dem unteren Rand
player_speed = 5            # Geschwindigkeit pro Frame

#geschoss eigentschaften
bullet_width = 5
bullet_height = 10
bullet_speed = 5
bullet_color = BCOLOR
bullets = [] 

# Haupt-Spielschleife
clock = pygame.time.Clock()  # Uhr für die Framerate
running = True               # Steuerung der Schleife

while running:
    clock.tick(60)          # Max. 60 Frames pro Sekunde
    win.fill(BLACK)         # Hintergrund mit Schwarz füllen
   
    # Alle Events abfragen (z.B. Fenster schließen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Wenn "X" gedrückt wird
            running = False             # Schleife beenden

    # Tasteneingaben abfragen
    keys = pygame.key.get_pressed()     # Aktuell gedrückte Tasten
    if keys[pygame.K_LEFT]:             # Wenn linke Pfeiltaste gedrückt
        player_x -= player_speed        # Spieler nach links bewegen
    if keys[pygame.K_RIGHT]:            # Wenn rechte Pfeiltaste gedrückt
        player_x += player_speed        # Spieler nach rechts bewegen
    if keys[pygame.K_DOWN]:            # Wenn rechte Pfeiltaste gedrückt
        player_y += player_speed 
    if keys[pygame.K_UP]:            # Wenn rechte Pfeiltaste gedrückt
        player_y -= player_speed 
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(player_x + player_width // 2 - bullet_width // 2, player_y - bullet_height, bullet_width, bullet_height)
        bullets.append(bullet)
    for bullet in bullets:
        bullet.y -= bullet_speed  # Move bullet upwards
        if bullet.y < 0:          # Remove bullet if it goes off-screen
            bullets.remove(bullet)       
    # bullet zeichnen
    for bullet in bullets:
        pygame.draw.(win, bullet)
    # Spieler innerhalb des Fensters halten
    player_x = max(0, min(WIDTH - player_width, player_x))  # Begrenzung links/rechts
    player_y = max(0, min(HEIGHT - player_height, player_y))  # Begrenzung links/rechts

    # Spieler-Quadrat zeichnen
    pygame.draw.rect(win, RED, (player_x, player_y, player_width, player_height))

    pygame.display.update()             # Anzeige aktualisieren

pygame.quit()               # Pygame sauber beenden
sys.exit()                  # Programm beenden