import time
import RPi.GPIO as GPIO
import sys, pygame
pygame.init()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
dc = 50
cy = 50
r = GPIO.PWM(11, (cy)) 
r.start(dc)
on = True
while on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False  

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dc -= 1
                p.ChangeDutyCycle(dc)
                print(dc)
            if event.key == pygame.K_DOWN:
                dc += 1
                p.ChangeDutyCycle(dc)
                print(dc)

p.stop()
GPIO.cleanup()
