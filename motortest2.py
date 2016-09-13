#!/usr/bin/env python2

import pygame
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
pygame.init()
screen = pygame.display.set_mode((480, 320))
done = False
speed = 75
mh = Adafruit_MotorHAT()
myMotor = mh.getMotor(3)
myMotor.setSpeed(speed)
t = 1
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


turnOffMotors()
while not done:
##        motor = 3
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                done = True
                        if event.key == pygame.K_UP:
                                myMotor.run(Adafruit_MotorHAT.FORWARD)
                        if event.key == pygame.K_DOWN:
                                myMotor.run(Adafruit_MotorHAT.BACKWARD)
                        if event.key == pygame.K_f:
                                myMotor.run(Adafruit_MotorHAT.FORWARD)
                        if event.key == pygame.K_b:
                                myMotor.run(Adafruit_MotorHAT.BACKWARD)
                        if event.key == pygame.K_s:
                                turnOffMotors()
                        if event.key == pygame.K_LEFT:
                                speed -=10
                                print speed
                                myMotor.setSpeed(speed)
                        if event.key == pygame.K_RIGHT:
                                speed +=10
                                print speed
                                myMotor.setSpeed(speed)
                        if event.key == pygame.K_m:
                                speed = 255
                                print 'Max speed'
                                print speed
                                myMotor.setSpeed(speed)
                        if event.key == pygame.K_5:
                                speed = 135
                                print speed
                                myMotor.setSpeed(speed)                        
                        if event.key == pygame.K_0:
                                speed = 0
                                print speed
                                myMotor.setSpeed(speed)
                        if event.key == pygame.K_9:
                                speed = 255
                                print speed
                                myMotor.setSpeed(speed)
                        if event.key == pygame.K_F1:
                                myMotor = mh.getMotor(1)
                                myMotor.setSpeed(speed)
                                print'motor 1'
                        if event.key == pygame.K_F2:
                                myMotor = mh.getMotor(2)
                                myMotor.setSpeed(speed)
                                print'motor 2'   
                        if event.key == pygame.K_F3:
                                myMotor = mh.getMotor(3)
                                myMotor.setSpeed(speed)
                                print'motor 3'
                        if event.key == pygame.K_F4:
                                myMotor = mh.getMotor(4)
                                myMotor.setSpeed(speed)
                                print'motor 4'


                                
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                                myMotor.run(Adafruit_MotorHAT.RELEASE)
                        if event.key == pygame.K_DOWN:
                                myMotor.run(Adafruit_MotorHAT.RELEASE)
  


        time.sleep(.01)

        

pygame.quit()
turnOffMotors()
