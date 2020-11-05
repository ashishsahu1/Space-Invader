import pygame

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

def player():
    screen.blit(playerImg,(playerX,playerY))

# Game loop
running = True
while running:
    screen.fill((15, 48, 87))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    player()

    
    pygame.display.update()