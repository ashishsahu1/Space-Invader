import pygame
from pygame.constants import KEYDOWN
import random

#initialise pygame module
pygame.init()

#creating screen (x,y)
screen = pygame.display.set_mode((800,600))

background = pygame.image.load('img/bg.png')

#title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('img/icon2.png')
pygame.display.set_icon(icon)

bulletImg = pygame.image.load('img/bullet.png')
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 0.05

# global bullet_state
bullet_State = 'ready'

def bullet(x,y):
    print("bullet")
    screen.blit(bulletImg, (x+16,y+10))
    global bullet_state
    bullet_state = "fire"

# def fire_bullet(x,y):
#     global bullet_state
#     bullet_state = 'fire'
#     screen.blit(bulletImg, (x+16,y+16))


#enemy
enemyImg = pygame.image.load('img/enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyXchange = 0.2
enemyYchange = 40
def enemy(enemyX,enemyY):
    screen.blit(enemyImg,(enemyX,enemyY))

#player
playerImg = pygame.image.load('img/player.png')
playerX = 370
playerY = 480
playerXchange = 0
# Ychange = 0
def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))

# Game loop
running = True
while running:

    #screen colour
    screen.fill((15, 48, 87))

    #background
    #screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    #checking keystroke is left or right
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.3
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.3
                
            if event.key == pygame.K_SPACE:
                bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0


    #player boundary check      
    playerX += playerXchange
    if playerX >= 736:
        playerX = 736
    elif playerX <=0:
        playerX = 0

    #enenmy movement
    enemyX += enemyXchange
    if enemyX  >= 736:
        enemyXchange = -0.2
        enemyY += enemyYchange
    elif enemyX  <=0:
        enemyXchange  = 0.2
        enemyY += enemyYchange


    if bullet_State == "fire":
        print("fire")
        bullet(playerX,bulletY)
        bulletY -= bulletYchange
    
    # playerY += Ychange
    player(playerX,playerY)
    


    enemy(enemyX,enemyY)

    pygame.display.update()