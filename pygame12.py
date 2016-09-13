import pygame

pygame.init()

done = False
is_blue = True
x = 0
y = 0
black = 0, 0, 0
size = width, height = 320, 320
image = 'bton2.png'
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((480, 320), pygame.FULLSCREEN)


def blitimg(image, size, color):
    global img
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)
    img = pygame.image.load(image)
    img = pygame.transform.smoothscale((img), (size))
    imgc = img.get_rect()
    imgc.center = background.get_rect().center
    background.blit(img, imgc)
    screen.fill(color)
    screen.blit(background, (x,y))
    pygame.display.flip()
    
while not done:

        blitimg(image, size, black)
        
        br = img.get_rect()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if br.collidepoint(pos):
                            exit(0)
                            
                                #is_blue = not is_blue

##                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
##                        is_blue = not is_blue
##

##        pressed = pygame.key.get_pressed()
##        
##        if pressed[pygame.K_UP]: y -= 3
##        if pressed[pygame.K_DOWN]: y += 3
##        if pressed[pygame.K_LEFT]: x -= 3
##        if pressed[pygame.K_RIGHT]: x += 3
##
##        if is_blue: color = (0, 128, 255)
##        else: color = (255, 100, 0)
##        pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
##        pygame.display.flip()
        clock.tick(60)
pygame.quit()
