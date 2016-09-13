import pygame
pygame.init()

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


   
done  = False
while done == False:

    blitimg(image, size, black)
    screen.blit(background, (x, y))
    bton(red, x, y)
    br = img.get_rect()
    pygame.display.flip()
   
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if br.collidepoint(pos):
                      done = True
    pressed = pygame.key.get_pressed()
                        
    if pressed[pygame.K_DOWN]:
        done = True
    clock.tick(60)
pygame.quit()
