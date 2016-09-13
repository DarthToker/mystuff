#! /usr/bin/env python

import os
import random
import time
import alsaaudio
import wave
import random
from creds import *
import requests
import json
import re
from memcache import Client

done = False
is_blue = True
x = 0
y = 0
black = 0, 0, 0
size = width, height = 320, 320
screensize = 480, 320
image = 'bton2.png'
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
#screen = pygame.display.set_mode((screensize), pygame.FULLSCREEN)
screen = pygame.display.set_mode(screensize)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)
red = (255,0,0)
white = (255,255,255)

def blitimg(image, size, color):
    global img
    global imgc
    img = pygame.image.load(image)
    img = pygame.transform.smoothscale((img), (size))
    imgc = img.get_rect()
    imgc.center = background.get_rect().center
    background.blit(img, imgc)
    #screen.fill(color)

def bton(color,x, y):
    button = pygame.draw.rect(background, color, (x,y,80,80), 0)
device = "plughw:1" # Name of your microphone/soundcard in arecord -L

#Setup
recorded = False
servers = ["127.0.0.1:11211"]
mc = Client(servers, debug=1)
path = os.path.realpath(__file__).rstrip(os.path.basename(__file__))



def internet_on():
    try:
        r =requests.get('https://api.amazon.com/auth/o2/token')
        print "Connection OK"
        return True
    except:
        print "Connection Failed"
        return False

    
def gettoken():
    token = mc.get("access_token")
    refresh = refresh_token
    if token:
        return token
    elif refresh:
        payload = {"client_id" : Client_ID, "client_secret" : Client_Secret, "refresh_token" : refresh, "grant_type" : "refresh_token", }
        url = "https://api.amazon.com/auth/o2/token"
        r = requests.post(url, data = payload)
        resp = json.loads(r.text)
        mc.set("access_token", resp['access_token'], 3570)
        return resp['access_token']
    else:
        return False
        

def alexa():
    url = 'https://access-alexa-na.amazon.com/v1/avs/speechrecognizer/recognize'
    headers = {'Authorization' : 'Bearer %s' % gettoken()}
    d = {
        "messageHeader": {
            "deviceContext": [
                {
                    "name": "playbackState",
                    "namespace": "AudioPlayer",
                    "payload": {
                        "streamId": "",
                        "offsetInMilliseconds": "0",
                        "playerActivity": "IDLE"
                    }
                }
            ]
        },
        "messageBody": {
            "profile": "alexa-close-talk",
            "locale": "en-us",
            "format": "audio/L16; rate=16000; channels=1"
        }
    }
    with open(path+'recording.wav') as inf:
        files = [
                ('file', ('request', json.dumps(d), 'application/json; charset=UTF-8')),
                ('file', ('audio', inf, 'audio/L16; rate=16000; channels=1'))
                ]   
        r = requests.post(url, headers=headers, files=files)
    if r.status_code == 200:
        for v in r.headers['content-type'].split(";"):
            if re.match('.*boundary.*', v):
                boundary =  v.split("=")[1]
        data = r.content.split(boundary)
        for d in data:
            if (len(d) >= 1024):
                audio = d.split('\r\n\r\n')[1].rstrip('--')
        with open(path+"response.mp3", 'wb') as f:
            f.write(audio)
        os.system('mpg123 -q {}1sec.mp3 {}response.mp3'.format(path, path))
    else:

        for x in range(0, 3):
            time.sleep(.2)
        
            time.sleep(.2)
        


while internet_on() == False:
        print "."
token = gettoken()
os.system('mpg123 -q {}1sec.mp3 {}hello.mp3'.format(path, path))
for x in range(0, 3):
        time.sleep(.1)
        time.sleep(.1)
alexaon = True
last = 1


   
done  = False
while done == False:
    

    
    blitimg(image, size, black)
    screen.blit(background, (x, y))
    bton(red, x, y)
    br = img.get_rect()
    pygame.display.flip()
    val = 1
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if br.collidepoint(pos):
                        val = 0
                    if val != last:
                            last = val
                            if val == 1 and recorded == True:
                                    rf = open(path+'recording.wav', 'w') 
                                    rf.write(audio)
                                    rf.close()
                                    inp = None
                                    alexa()
                            elif val == 0:
                                    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, device)
                                    inp.setchannels(1)
                                    inp.setrate(16000)
                                    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
                                    inp.setperiodsize(500)
                                    audio = ""
                                    l, data = inp.read()
                                    if l:
                                            audio += data
                                    recorded = True
                    elif val == 0:
                            l, data = inp.read()
                            if l:
                                    audio += data
           



                        
    pressed = pygame.key.get_pressed()
                        
    if pressed[pygame.K_DOWN]:
        done = True
    clock.tick(60)
pygame.quit()
