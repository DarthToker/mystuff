#!/usr/bin/env python2
import pygame
import pygame.camera
import pygame.image
import sys
import time
pygame.camera.init()


size = width, height = 320, 320
black = 0, 0, 0
x=0
y=0
screen = pygame.display.set_mode((size))
pygame.display.set_caption("pyGame Camera View")

cameras = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameras[0])
webcam.start()
def pic():
    screen.fill(black)
    img = webcam.get_image()
    img = pygame.transform.smoothscale(img, (size))
    screen.blit(img, (0,0))
    pygame.display.flip()
    img = webcam.get_image()

pic()
time.sleep(5)
pic()
time.sleep(2)
