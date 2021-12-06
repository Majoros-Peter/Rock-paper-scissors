import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Rock-paper-scissors")
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTERX= WIDTH / 2
CENTERY = HEIGHT / 2
FPS = 60

ROCK = pygame.image.load("Rock.png")
PAPER = pygame.image.load("Paper.png")
SCISSORS = pygame.image.load("Scissors.png")
ROCK_PLAYER = pygame.image.load("Rock_player.png")
PAPER_PLAYER = pygame.image.load("Paper_player.png")
SCISSORS_PLAYER = pygame.image.load("Scissors_player.png")

UNSIZED_BACKGROUND = pygame.image.load("Background.jpg")
BACKGROUND = pygame.transform.scale(UNSIZED_BACKGROUND, (WIDTH, HEIGHT))
HEADER = (0, 0, WIDTH, 100)

font = pygame.font.Font('freesansbold.ttf', 40)
header_text = font.render("KŐ - PAPÍR - OLLÓ", True, white, (30, 30, 30))
font = pygame.font.Font('freesansbold.ttf', 20)
start_text = font.render("Induljon a játék!", True, black)
textRect_header = header_text.get_rect()
textRect_start = start_text.get_rect()
start_keret = pygame.draw.rect(WIN, black, (int(CENTERX - 125), int(CENTERY - 50), 300, 75), 2, 10)
start_text_hover = font.render("Induljon a játék!", True, white)

game_started = False
player_score = 0
pc_score = 0
font = pygame.font.Font('freesansbold.ttf', 30)
jatekos = font.render("Játékos", True, black)
jatekos_pont = font.render(str(player_score), True, black)
szamitogep = font.render("Számítógép", True, black)
szamitogep_pont = font.render(str(pc_score), True, black)
font = pygame.font.Font('freesansbold.ttf', 40)
valassz = font.render("Válassz! Kő, papír vagy olló!", True, black)
font = pygame.font.Font('freesansbold.ttf', 20)
ko_gomb = ("KŐ", True, black)
ko_gomb_hover = ("KŐ", True, white)
ko_gomb_keret = pygame.draw.rect(WIN, black, (int(CENTERX - 130), int(CENTERY - 200), 0, int(CENTERY)), 1, 10)
papir_gomb = ("PAPÍR", True, black)
papir_gomb_hover = ("PAPÍR", True, white)
papir_gomb_keret = pygame.draw.rect(WIN, black, (int(CENTERX), int(CENTERY- 200), 0, int(CENTERY)), 1, 10)
ollo_gomb = ("OLLÓ", True, black)
ollo_gomb_hover = ("OLLÓ", True, white)
ollo_gomb_keret = pygame.draw.rect(WIN, black, (int(CENTERX + 130), int(CENTERY - 200), 0, int(CENTERY)), 1, 10)

##################################################################################################################################################################################################################
##################################################################################################################################################################################################################

def draw_window():
    WIN.blit(BACKGROUND, (0, 60))

    # Ez jeleníti meg felül a "KŐ - PAPÍR - OLLÓ" feliratot
    pygame.draw.rect(WIN, (30, 30, 30), (0, 0, WIDTH, 60))
    textRect_header.midtop = (CENTERX - 150, 10)
    WIN.blit(header_text, textRect_header.midtop)

    # Játék elindítása előtt megjeleníti az "Induljon a játék!" gombot
    pygame.draw.rect(WIN, black, (int(CENTERX - 125), int(CENTERY - 50), 300, 75), 2, 10)
    textRect_start.center = (CENTERX - 50, CENTERY - 25)
    WIN.blit(start_text, textRect_start.center)

    #Ez csinálja a :hover effektet (még nem jó)
    if start_keret.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(WIN, black, (int(CENTERX - 125), int(CENTERY - 50), 300, 75), False, 10)
        WIN.blit(start_text_hover, textRect_start.center)
    pygame.display.update()

##################################################################################################################################################################################################################

def jatek():
    #Ez eltünteti az "Induoljon a játék" feliratot
    global game_started
    game_started = True

    #Ezek jelennek meg amikor elindul a játék
    WIN.blit(BACKGROUND, (0, 60))
    WIN.blit(ROCK, (CENTERX + 50, CENTERY - 150))
    WIN.blit(ROCK_PLAYER, (CENTERX - 250, CENTERY - 150))
    pygame.draw.rect(WIN, black, (20, 150, 500, 150), 4, 40)
    WIN.blit(jatekos, (50, 175))
    WIN.blit(jatekos_pont, (90, 225))
    WIN.blit(szamitogep, (300, 175))
    WIN.blit(szamitogep_pont, (370, 225))
    WIN.blit(valassz, (700, 150))

    # KŐ gomb
    pygame.draw.rect(WIN, black, (int(CENTERX - 130), int(CENTERY - 200), 0, int(CENTERY)), 1, 10)
    ko_gomb_keret.center= (int(CENTERX - 150), int(CENTERY - 200))
    WIN.blit(ko_gomb, ko_gomb_keret.center)

    # PAPÍR gomb
    pygame.draw.rect(WIN, black, (int(CENTERX), int(CENTERY- 200), 0, int(CENTERY)), 1, 10)
    papir_gomb_keret.center = (int(CENTERX), int(CENTERY - 200))
    WIN.blit(papir_gomb, papir_gomb_keret.center)

    #OLLÓ gomb
    pygame.draw.rect(WIN, black, (int(CENTERX + 130), int(CENTERY - 200), 0, int(CENTERY)), 1, 10)
    ollo_gomb_keret.center = (int(CENTERX + 150), int(CENTERY - 200))
    WIN.blit(ollo_gomb, ollo_gomb_keret.center)

    pygame.display.update()

##################################################################################################################################################################################################################

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        if game_started == False:
            draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_ESCAPE]:
                run = False
            if start_keret.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                jatek()

    pygame.quit()

if __name__ == '__main__':
    main()
