import sys, pygame
pygame.init()

size = width, height = 200, 200
speed = [2, 2]
black = 0, 0, 0
x=60
y=60
screen = pygame.display.set_mode(size)

ball = pygame.image.load("nu.png")
smile  = pygame.image.load("sm2.png")
frn  = pygame.image.load("frn.png")
kiss  = pygame.image.load("kiss.png")

ballrect = ball.get_rect()
clock = pygame.time.Clock()
balling = False
while not balling:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            balling = True

##    ballrect = ballrect.move(speed)
##    if ballrect.left < 0 or ballrect.right > width:
##        speed[0] = -speed[0]
##    if ballrect.top < 0 or ballrect.bottom > height:
##        speed[1] = -speed[1]
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        screen.fill(black)
        screen.blit(smile, (x,y))
        pygame.display.flip()
        clock.tick(120)
    if pressed[pygame.K_DOWN]:
        screen.fill(black)
        screen.blit(frn, (x,y))
        pygame.display.flip()
        clock.tick(60)
    if pressed[pygame.K_LEFT]:
        screen.fill(black)
        screen.blit(kiss, (x,y))
        pygame.display.flip()
        clock.tick(60)        
    else:
        screen.fill(black)
        screen.blit(ball, (x,y))
        pygame.display.flip()
        clock.tick(60)
pygame.quit()

