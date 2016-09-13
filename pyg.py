# -*- coding: utf-8-*-
#import jasperpath
import sys, pygame
import time
import pygame.camera
from pygame.locals import *
pygame.init()
pygame.camera.init()
pygame.display.set_caption('jarvis')
pygame.mouse.set_visible(False)



image = 'nu.png'
size = width, height = 320, 320
screensize = 480, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0

webcam = pygame.camera.Camera("/dev/video0",(640,480))
webcam.start()

class Pygm(object):

    def __init__(self):
        
        #self.screen = pygame.display.set_mode((screensize), pygame.FULLSCREEN)
        #pygame.camera.init

        self.screen = pygame.display.set_mode(screensize)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(black)
##        self.cam = pygame.camera.Camera('/dev/video0', (screensize))
##        self.cam.start()

##        self.cameras = pygame.camera.list_cameras()
##        self.webcam = pygame.camera.Camera(self.cameras[0])
##        self.webcam.start()
##        self.cam = self.webcam

        
    def fbackground(self, color):
        self.background.fill(color)

    def bbackground(self):
        self.screen.blit(self.background, (0, 0))
    
    def flip(self):
        pygame.display.flip()

    def blitimg(self, image, size, color, x, y):

        self.background.fill(color)
        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.imgc = self.img.get_rect()
        self.imgc.center = self.background.get_rect().center
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))
        pygame.display.flip()
        imgc = self.imgc
        return imgc


    def blittxt(self, txt, txts, color, bcolor):

        self.background.fill(bcolor)
        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.textx = self.txt.get_rect()
        self.textx.center = self.background.get_rect().center
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def blitimg2(self, image, size,  x, y):

        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.imgc = self.img.get_rect()
        self.imgc.center = self.background.get_rect().center
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))
        pygame.display.flip()

    def blittxt2(self, txt, txts, color, bcolor):

        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.textx = self.txt.get_rect()
        self.textx.center = self.background.get_rect().center
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        
    def blittxt3(self, txt, txts, color, tx, ty):

        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.textx = self.txt.get_rect()
        self.textx.center = (tx, ty)
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()


    def bton(self, color, bx, by, txt, txts, tcolor):

        self.font = pygame.font.Font(None, txts)
        self.button = pygame.draw.rect(self.background, color, (bx,by,80,80), 0)
        self.txt = self.font.render("%s" %txt, True, (tcolor))
        self.bc = self.txt.get_rect()
        self.bc.center = self.button.center
        self.background.blit(self.txt, self.bc)
        pygame.display.flip()
        
    def bton2(self, color, bx, by, txt, txts, tcolor):
        font = pygame.font.Font(None, txts)
        button = pygame.draw.rect(self.background, color, (bx,by,80,80), 0)
        txt = font.render("%s" %txt, True, (tcolor))
        bc = txt.get_rect()
        bc.center = button.center
        self.background.blit(txt, bc)

    def takepic(self):
        webcam.start()

        img = webcam.get_image()
        pygame.image.save(img,'abc2.jpg')
        screen.blit(img, (0,0))
        pygame.display.flip()
        webcam.stop()
        print'ididsomething'



        

##        self.background.fill(color)
##        self.img = self.cam.get_image()
##        pygame.image.save(self.img,'abc2.jpg')
##
##        self.img = pygame.transform.smoothscale((self.img), (screensize))
##        self.imgc = self.img.get_rect()
##        self.imgc.center = self.background.get_rect().center
##        self.background.blit(self.img, self.imgc)
##        self.screen.blit(self.background, (x,y))
##        pygame.display.flip()


##a.blitimg2(image, size, black, x, y)
##a.flip()
##time.sleep(3)
##
##a.blittxt2('test', 200, red, black)
##a.flip()
##time.sleep(3)
##a.fbackground(black)
##a.bbackground()
##a.flip()
##time.sleep(3)
a = Pygm()
##
##
##a.fbackground(black)
##a.blitimg('dtoker.jpg', size, black, x, y)
##a.blittxt3('TokerWare', 50, red, 240, 300)


##time.sleep(5)
##a.blitimg(image, size, black, x, y)
a.takepic 
##
time.sleep(5)
##
pygame.quit()
