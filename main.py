import pygame

#initialise pygame module
pygame.init()

#creating screen
screen = pygame.display.set_mode((800,600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False