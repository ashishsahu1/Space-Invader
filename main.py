import pygame
from pygame.constants import KEYDOWN
import random

#initialise pygame module
pygame.init()

#creating screen (x,y)
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('img/icon2.png')
pygame.display.set_icon(icon)

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    #checking keystroke is left or right
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.3
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.3

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

    
    # playerY += Ychange
    player(playerX,playerY)

    enemy(enemyX,enemyY)

    pygame.display.update()