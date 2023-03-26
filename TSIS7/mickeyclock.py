import pygame
import datetime

pygame.init()

HEIGHT = 800
WIDTH = 800
FPS = 60

screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("mickeyclock")
clock = pygame.time.Clock()

mickeyclock = pygame.image.load("./images/background.jpg")
minure_arrow = pygame.image.load("./images/min.png")
second_arrow = pygame.image.load("./images/sec.png")

def time(t):
    return 360 - t * 6

def rotateee(surface, image, left_pos, angle):
    transformed_image = pygame.transform.rotate(image, angle)
    new_figure = transformed_image.get_rect(center = image.get_rect(topleft = left_pos).center)

    surface.blit(transformed_image, new_figure)

running = True

while running:

    clock.tick(FPS)

    for i in pygame.event.get():
        if i == pygame.QUIT:
            running = False
    screen.blit(mickeyclock, (0,0))
    t = datetime.datetime.now()
    angle_sec = time(t.second)
    angle_min = time(t.minute)
    rotateee(screen, second_arrow, (255, 150), angle_sec)
    rotateee(screen, minure_arrow, (255, 150), angle_min)

    pygame.display.flip()

pygame.quit()
    
