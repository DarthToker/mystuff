#!/usr/bin/env python2

import time
import random
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)#red
GPIO.setup(37, GPIO.OUT)#blue
GPIO.setup(40, GPIO.OUT)#green

T = 0.01
g = GPIO.PWM(40, 50)
r = GPIO.PWM(38, 50)
b = GPIO.PWM(37, 50) 
g.start(0)
r.start(0)
b.start(0)

def gup():
    for dc in range(0, 101, 5):
        g.ChangeDutyCycle(dc)
        time.sleep(T)

def gd():
    for dc in range(100, -1, -5):
        g.ChangeDutyCycle(dc)
        time.sleep(T)
def rup():
    for dc in range(0, 101, 5):
        r.ChangeDutyCycle(dc)
        time.sleep(T)

def rd():
    for dc in range(100, -1, -5):
        r.ChangeDutyCycle(dc)
        time.sleep(T)
def bup():
    for dc in range(0, 101, 5):
        b.ChangeDutyCycle(dc)
        time.sleep(T)

def bd():
    for dc in range(100, -1, -5):
        g.ChangeDutyCycle(dc)
        time.sleep(T)
def ud():
        gup()
        bup()
        rup()
        gd()
        bd()
        rd()


try:
    while 1:
        lon = [rup(), gup(), bup()]
        rlon = random.choice(lon)
        loff = [rd(), gd(), bd()]
        rloff = random.choice(loff)
        rlon
        rloff

        
        

except KeyboardInterrupt:
    pass
r.stop()
g.stop()
b.stop()

GPIO.cleanup()
