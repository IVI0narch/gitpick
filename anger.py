import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((300,300))
circle(screen,(255, 255, 0), (150, 150), 150) 
circle(screen,(255, 0, 0), (75, 75), 20)
circle(screen,(255, 0, 0), (225, 75), 20)
circle(screen,(0, 0, 0), (75, 75), 10)
circle(screen,(0, 0, 0), (225, 75), 15)
rect(screen, (0, 0, 0), (80, 190, 140, 20))
line(screen, (0, 0, 0), (65, 25), (130, 70), 20) 
line(screen, (0, 0, 0), (160, 85), (220, 30), 20)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
