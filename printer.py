import pygame
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import time
pygame.init()
screen = pygame.display.set_mode((480, 320))
done = False
mh = Adafruit_MotorHAT()
myMotor = mh.getMotor(3)
myMotor.setSpeed(200)
t = .1
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

step1 = mh.getStepper(150, 1)       
step1.setSpeed(20)
turnOffMotors()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
                step1.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
        if pressed[pygame.K_DOWN]:
                step1.step(10, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
        if pressed[pygame.K_LEFT]:
                myMotor.run(Adafruit_MotorHAT.FORWARD)
                time.sleep(t)
        if pressed[pygame.K_RIGHT]:
                myMotor.run(Adafruit_MotorHAT.BACKWARD)
                time.sleep(t)

        if pressed[pygame.K_ESCAPE]:
                done = True
        else: 
                turnOffMotors()
##        time.sleep(0.1)
        

pygame.quit()
turnOffMotors()
