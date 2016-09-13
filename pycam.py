#!/usr/bin/env python2
import pygame
import pygame.camera
import pygame.image
import sys
pygame.init()
pygame.camera.init()

cameras = pygame.camera.list_cameras()

print "Using camera %s ..." % cameras[0]

webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = webcam.get_image()
pygame.image.save(img,'abc.jpg')

WIDTH = img.get_width()
HEIGHT = img.get_height()
print (HEIGHT)
print (WIDTH)

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("pyGame Camera View")

while True :
 for e in pygame.event.get() :
     if e.type == pygame.QUIT :
         sys.exit()

 # draw frame
 screen.blit(img, (0,0))
 pygame.display.flip()
 # grab next frame    
 img = webcam.get_image()
pygame.quit()
