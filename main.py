import math
import pygame
from turtle import Screen
import sys

#pygame settings
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("graphic calculator")
WINW = WINH = 600
windowSurface = pygame.display.set_mode((WINW, WINH))
mainClock = pygame.time.Clock()
FPS = 1000
font = pygame.font.Font('assets/PressStart2P-regular.ttf', 25)

#colors
RED = (200, 0, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

screen.fill("white")
pygame.draw.rect(screen, GRAY, (300, 0, 4, 600))
pygame.draw.rect(screen, GRAY, (0, 296, 600, 4))


#PRINCIPAL PARAMITERS
scale = 1
Zoom = 1
x = (-300/Zoom)
x3 = 0
y3 = 0


#while true
while True:
    #if x goes of the board, stop the computation
    if not x > 300:
        x += (0.1/Zoom)

    #draw the lines
    if x3 < 600:
        x3 += 1*Zoom

    if y3 < 600:
        y3 += 1*Zoom*scale

    #x2 is used in draw
    x2 = x+300
    
    #type your function like x**2+4*x+16
    Function = x

    #using the paramiters
    Function = (Function*Zoom*scale)

    pygame.draw.rect(screen, BLACK, (300, y3-4, 4, 4))
    pygame.draw.rect(screen, BLACK, (x3, 300-4, 4, 4))
    
    if Function <= 600 and Function >= -600: #if function goes of the board, stop the computation
        pygame.draw.rect(screen, RED,((x2*Zoom)-((Zoom - 1)*300), -Function+ 295, 5, 5)) #draw using rect, the graphic line

    #CANVAS

    Canva1 = font.render(str(int(Zoom)), True, (BLACK))
    screen.blit((Canva1), (5, 570))


    Canva2 = font.render(str(scale), True, (BLACK))
    screen.blit((Canva2), (5, 10))
     

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mainClock.tick(FPS)
    pygame.display.update()


