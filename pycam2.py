#!/usr/bin/env python2
import pygame
import pygame.camera
import pygame.image
import sys
import time
pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode( (480, 320) )
pygame.display.set_caption("pyGame Camera View")


webcam = pygame.camera.Camera("/dev/video0",(640,480))


def get():
    webcam.start()

    img = webcam.get_image()
    pygame.image.save(img,'abc2.jpg')
    screen.blit(img, (0,0))
    pygame.display.flip()
    webcam.stop()

print"1"
get()

time.sleep(5)
##print"2"
##get()
time.sleep(5)

pygame.quit()
