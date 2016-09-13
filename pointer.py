#!/usr/bin/env python
import RPi.GPIO as GPIO

import usb.core
import usb.util
import time
USB_VENDOR  = 0x047d # Rii
USB_PRODUCT = 0x2012 # Mini Wireless Keyboard

USB_IF      = 0 # Interface
USB_TIMEOUT = 5 # Timeout in MS

BTN_LEFT  = 75
BTN_RIGHT = 78
BTN_DOWN  = 5
BTN_UP    = 62
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

dc = 50
cy = 50
r = GPIO.PWM(11, (cy))
g = GPIO.PWM(13, (cy)) 
y = GPIO.PWM(32, (cy)) 

r.start(dc)
g.start(dc)
y.start(dc)
dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)
endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(USB_IF) is True:
  dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF)

def cd():
  r.ChangeDutyCycle(dc)
  g.ChangeDutyCycle(dc)
  y.ChangeDutyCycle(dc)

def cff():
  r.ChangeFrequency(cy)
  g.ChangeFrequency(cy)
  y.ChangeFrequency(cy)


  
while True:
    control = None
    try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        #print(control)
    except:
        pass

    if control != None:
        if BTN_DOWN in control:
            print'down'
            dc -= 1
            cd()
            print(dc)
        if BTN_UP in control:
            print'up'
            dc += 1
            cd()
            print(dc)
        if BTN_LEFT in control:
            print'left'
            cy -= 1
            cff()
            print(cy)
        if BTN_RIGHT in control:
            print'right'
            cy += 1
            cff()
            print(cy)
    time.sleep(0.02)
