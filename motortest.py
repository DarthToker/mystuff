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
myMotor.setSpeed(0)
t = 1
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
	if pressed[pygame.K_ESCAPE]:
		done = True
	print "Forward! "
	myMotor.run(Adafruit_MotorHAT.FORWARD)

	print "\tSpeed up..."
	for i in range(255):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "Backward! "
	myMotor.run(Adafruit_MotorHAT.BACKWARD)

	print "\tSpeed up..."
	for i in range(255):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "Release"
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)



##        time.sleep(0.1)
	

pygame.quit()
turnOffMotors()
