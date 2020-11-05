import pygame
from pygame.constants import KEYDOWN

#initialise pygame module
pygame.init()

#creating screen (x,y)
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('img/icon2.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('img/space.png')
playerX = 370
playerY = 480
Xchange = 0
Ychange = 0

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
                Xchange = -0.3
            if event.key == pygame.K_RIGHT:
                Xchange = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Xchange = 0
            

    playerX += Xchange
    playerY += Ychange
    player(playerX,playerY)


    pygame.display.update()