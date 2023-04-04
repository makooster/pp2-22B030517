import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LOSS_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
SCORE = 0
clock = pygame.time.Clock()
background = pygame.image.load('./materials/AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)
background_sound = pygame.mixer.Sound("./materials/background.wav")
crush_sound = pygame.mixer.Sound("./materials/crash.wav")




class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 7
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)

    
coins = pygame.sprite.Group()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./materials/cent.png")
        self.speed = 7
        self.resized_image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.resized_image.get_rect()
        if WIDTH - self.rect.width > self.rect.width:
            x = random.randint(self.rect.width, WIDTH - self.rect.width)
        else:
            x = random.randint(WIDTH - self.rect.width, self.rect.width)
        self.rect.center = (x, 0)

    def draw(self, surface):
        surface.blit(self.resized_image, self.rect)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )
    def collide(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.kill()  # Remove the sprite from all sprite groups it belongs to
            return True
        return False
    
def main():
    #creating all characters and resources
    global coins
    running = True
    player = Player()
    enemy = Enemy()
    coin = Coin()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    coins.add(coin)
    background_sound.play(-1)

    while running:
        global SCORE
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f"Your score: {SCORE}", True, WHITE)
        SCREEN.blit(score, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()
        
        # creating a new coin instead of deleted one
        for coin in coins:
            if coin.collide(player):
                coins.remove(coin)
                SCORE += 1
                coins.add(Coin())

        coin.draw(SCREEN)
        coin.update()
        player.draw(SCREEN)
        enemy.draw(SCREEN)

        if pygame.sprite.spritecollide(player, enemies, False):
            background_sound.stop() # stop playing the background music
            crush_sound.play() # play the crash sound effect
            pygame.time.wait(2000)
            
            running = False
        
        pygame.display.flip()
        clock.tick(60)

main()