#!/usr/bin/env python2
import sys, pygame
pygame.init()
from emogdefs import *
size = width, height = 320, 320
black = 0, 0, 0
x=0
y=0
screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
clock = pygame.time.Clock()
balling = False
while not balling:
    screen.fill(black)
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            balling = True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    kiss()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    smile()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    frn()
                                             
        else:
            nu()

pygame.quit()

