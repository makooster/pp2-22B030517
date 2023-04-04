import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

# Create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Simple Paint Program")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set default brush color
brush_color = WHITE

# Set default brush size
brush_size = 5

# Set default mode to draw
draw_mode = True

# Define brush class
class Brush:
    def __init__(self):
        self.pos = (0, 0)
        self.size = brush_size
        self.color = brush_color
    
    def draw_circle(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.size)

    def draw_rect(self, surface):
        rect = pygame.Rect(self.pos, (self.size, self.size))
        pygame.draw.rect(surface, self.color, rect)
    
    def update_pos(self, pos):
        self.pos = pos

# Create brush object
brush = Brush()

clock = pygame.time.Clock()

running = True


while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                brush.update_pos(event.pos)
                draw_mode = True
            elif event.button == 3: # Right mouse button
                draw_mode = False
        elif event.type == pygame.MOUSEBUTTONUP:
            draw_mode = False
        elif event.type == pygame.MOUSEMOTION:
            if draw_mode:
                brush.update_pos(event.pos)

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            screen.fill(WHITE)
        elif keys[pygame.K_r]:
            brush.color = RED
        elif keys[pygame.K_g]:
            brush.color = GREEN
        elif keys[pygame.K_b]:
            brush.color = BLUE
        elif keys[pygame.K_1]:
            brush.size = 10
        elif keys[pygame.K_2]: 
            brush.size = 20
        elif keys[pygame.K_3]:
            brush.size = 30
        elif keys[pygame.K_s]:
            brush.draw_rect(screen)
        elif keys[pygame.K_e]:
            brush.draw_circle(screen)

    pygame.display.update()

    
    clock.tick(60)


pygame.quit()