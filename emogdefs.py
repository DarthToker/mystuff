import pygame

size = width, height = 320, 320
black = 0, 0, 0
x=0
y=0
screen = pygame.display.set_mode(size)

def nu():
    nu = pygame.image.load("nu.png")
    nu = pygame.transform.smoothscale(nu, (size))
    screen.fill(black)
    screen.blit(nu, (x,y))
    pygame.display.flip()

def smile():    
    smile  = pygame.image.load("sm2.png")
    smile = pygame.transform.smoothscale(smile, (size))
    screen.fill(black)
    screen.blit(smile, (x,y))
    pygame.display.flip()

def frn():                    
    frn  = pygame.image.load("frn.png")
    frn = pygame.transform.smoothscale(frn, (size))
    screen.fill(black)
    screen.blit(frn, (x,y))
    pygame.display.flip()
    
def kiss():    
    kiss  = pygame.image.load("kiss.png")
    kiss = pygame.transform.smoothscale(kiss, (size))
    screen.fill(black)
    screen.blit(kiss, (x,y))
    pygame.display.flip()

def ang():
    ang  = pygame.image.load("ang.png")
    ang = pygame.transform.smoothscale(ang, (size))
    screen.fill(black)
    screen.blit(ang, (x,y))
    pygame.display.flip()

def think():
    think  = pygame.image.load("think.png")
    think = pygame.transform.smoothscale(think, (size))
    screen.fill(black)
    screen.blit(think, (x,y))
    pygame.display.flip()






    
