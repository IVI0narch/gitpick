import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((300, 400))


def background():
    '''
    рисуем фон картинки

    '''
    polygon(screen, (119, 186, 208), [(0, 0), (0, 100), (50, 50),
                                      (100, 70), (120, 65), (130, 100),
                                      (160, 140), (210, 111), (250, 100),
                                      (300, 120), (300, 0)])
    polygon(screen, (120, 120, 120), [(0, 200), (0, 100), (50, 50),
                                      (100, 70), (120, 65), (130, 100),
                                      (160, 140), (210, 111), (250, 100),
                                      (300, 120), (300, 220), (250, 230),
                                      (100, 250)])
    polygon(screen, (181, 221, 144), [(0, 200), (250, 230), (300, 220),
                                      (300, 400), (0, 400)])


white = (255, 255, 255)
yellow = (255, 255, 0)


def flower(x, y, size):
    '''
    x, y - координаты центра цветка
    size размер цветка (0,100)
    рисует цветок с 8 лепестками

    '''
    circle(screen, yellow, (x, y), int(0.85*size))
    circle(screen, white, (int(x + 0.75*size), int(y + 0.75*size)), int(0.4*size))
    circle(screen, white, (int(x - 0.75*size), int(y + 0.75*size)), int(0.4*size))
    circle(screen, white, (int(x + 0.75*size), int(y - 0.75*size)), int(0.4*size))
    circle(screen, white, (int(x - 0.75*size), int(y - 0.75*size)), int(0.4*size))
    circle(screen, white, (int(x + size), y), int(0.4*size))
    circle(screen, white, (int(x - size), y), int(0.4*size))
    circle(screen, white, (x, int(y + size)), int(0.4*size))
    circle(screen, white, (x, int(y - size)), int(0.4*size))


def flower_bed(x, y, size):
    '''
    x, y - координаты центра клумбы
    size - размер клумбы
    рисует клумбу с 4 цветками

    '''
    circle(screen, (125, 225, 82), (x, y), size)
    flower(int(x + 0.4*size), int(y + 0.4*size), int(size*0.2))
    flower(int(x - 0.4*size), int(y - 0.5*size), int(size*0.3))
    flower(int(x - 0.3*size), int(y + 0.5*size), int(size*0.2))
    flower(int(x + 0.4*size), int(y - 0.3*size), int(size*0.3))


def shrek(x, y, size):
    '''
    x, y - координаты левого верхнего угла прямоугольника,
                на который натянуто "тело" единорога
    size - ширина тела единорога
    рисует единорога

    '''
    ellipse(screen, white, (x, y, size, int(0.3*size)))
    ellipse(screen, white, (x, int(y + 0.2*size),
                            int(0.1*size), int(0.5*size)))
    ellipse(screen, white, (int(x + 0.2*size), int(y + 0.15*size),
                            int(0.1*size), int(0.5*size)))
    ellipse(screen, white, (int(x + 0.7*size), int(y + 0.1*size),
                            int(0.1*size), int(0.5*size)))
    ellipse(screen, white, (int(x + 0.85*size), int(y + 0.2*size),
                            int(0.1*size), int(0.5*size)))
    ellipse(screen, white, (int(x + 0.85*size), int(y - 0.3*size),
                            int(0.2*size), int(0.5*size)))
    ellipse(screen, white, (int(x + 0.85*size), int(y - 0.4*size),
                            int(0.4*size), int(0.2*size)))
    ellipse(screen, (201, 120, 245), (int(x + 0.95*size), int(y - 0.38*size),
                                      int(0.1*size), int(0.1*size)))
    ellipse(screen, (1, 2, 5), (int(x + 0.97*size), int(y - 0.35*size),
                                int(0.05*size), int(0.05*size)))
    ellipse(screen, white, (int(x + 0.97*size), int(y - 0.37*size),
                            int(0.05*size), int(0.05*size)))
    circle(screen, white, (x, int(y + 0.7*size)), int(0.07*size))
    circle(screen, white, (int(x + 0.2*size), int(y + 0.65*size)), int(0.07*size))
    circle(screen, white, (int(x + 0.7*size), int(y + 0.6*size)), int(0.07*size))
    circle(screen, white, (int(x + 0.85*size), int(y + 0.7*size)), int(0.07*size))


background()
# рисуем клумбы и единорогов
flower_bed(250, 320, 40)
flower_bed(50, 230, 20)
flower_bed(180, 250, 30)
shrek(50, 300, 120)
shrek(70, 200, 40)
shrek(200, 250, 60)
shrek(60, 235, 80)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
