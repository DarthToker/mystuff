#!/usr/bin/env python2


import pygame
import time

pygame.init()

done = False
x = 0
y = 0
black = 0, 0, 0
width, height = 320, 320
image = 'ang.png'
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((480, 320))
screen.fill(black)
background = pygame.Surface(screen.get_size())
background = background.convert()

def blitimg(image, width, height, color, deg):
    img = pygame.image.load(image)
    img = pygame.transform.smoothscale((img), (width, height))
    img = pygame.transform.rotate(img, deg)
    imgc = img.get_rect()
    imgc.center = background.get_rect().center
    background.fill(black)

    background.blit(img, imgc)
    screen.blit(background, (x,y))
    pygame.display.flip()
try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()

        deg = 0
        for i in range(360):
            deg -=1
            blitimg(image, width, height, black, deg)
        for i in range(320):
            width -=1
            height -=1
            blitimg(image, width, height, black, deg)
        for i in range(320):
            width +=1
            height +=1
            blitimg(image, width, height, black, deg)
except KeyboardInterrupt:
    pygame.quit()
