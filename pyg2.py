import pygame


pygame.init()


display_width = 200
display_height = 200

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('jarvis')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('nu.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (60)
y = (60)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()

