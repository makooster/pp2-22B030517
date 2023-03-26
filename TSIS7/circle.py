import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255,255,255)
x = WIDTH // 2
y = HEIGHT // 2

pygame.display.set_caption("circle")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True
while running:
    for i in pygame.event.get():
        if i == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    clock.tick(FPS)
    pygame.draw.circle(screen, (255,0,0), (x, y), 25)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x + 25 < WIDTH:
        x += 20
    if keys[pygame.K_LEFT] and x > 25:
        x -= 20
    if keys[pygame.K_UP] and y > 25:
        y -= 20
    if keys[pygame.K_DOWN] and y + 25 < HEIGHT:
        y += 20
    pygame.display.flip()

pygame.quit()
    
    
