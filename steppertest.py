import pygame
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import time
pygame.init()
screen = pygame.display.set_mode((480, 320))
done = False
mh = Adafruit_MotorHAT()

def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

step1 = mh.getStepper(20, 1)       
step1.setSpeed(30)
step2 = mh.getStepper(20, 2)       
step2.setSpeed(30)
turnOffMotors()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
                step1.step(1, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
        if pressed[pygame.K_DOWN]:
                step1.step(1, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
        if pressed[pygame.K_LEFT]:
                step2.step(1, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)

        if pressed[pygame.K_RIGHT]:
                step2.step(1, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.SINGLE)

        if pressed[pygame.K_ESCAPE]:
                done = True
                
        turnOffMotors()
##        time.sleep(0.1)
        

pygame.quit()
turnOffMotors()
