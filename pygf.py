import pygame

size = width, height = 320, 320
black = 0, 0, 0
x=0
y=0
screensize = 480, 320
#screen = pygame.display.set_mode((screensize), pygame.FULLSCREEN)
screen = pygame.display.set_mode(screensize)


def blitimg(image, size, color):
    global img
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color)
    img = pygame.image.load(image)
    img = pygame.transform.smoothscale((img), (size))
    imgc = img.get_rect()
    imgc.center = background.get_rect().center
    background.blit(img, imgc)
    screen.fill(color)
    screen.blit(background, (x,y))
    pygame.display.flip()
    return img
    

def blittxt(txt, txts, color, bcolor):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(bcolor)
    font = pygame.font.Font(None, txts)
    txt = font.render("%s" %txt, True, (color))
    textx = txt.get_rect()
    textx.center = background.get_rect().center
    background.blit(txt, textx)
    screen.fill(color)
    screen.blit(background, (0, 0))
    pygame.display.flip()

#def blitbton():
    
