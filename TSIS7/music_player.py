import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60
# WHITE = (255,255,255)

playlist = ("./music/m1.mp3", "./music/m2.mp3", "./music/m3.mp3")
image = pygame.image.load("./images/music_player.png")

pygame.display.set_caption("mp3 player")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.blit(image, (0,0))
clock = pygame.time.Clock()
running = True
i = 0
pygame.mixer.music.load(playlist[i])
pygame.mixer.music.play(1)
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                i += 1
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play(1)
            if event.key == pygame.K_LEFT:
            # pygame.mixer.music.rewind()
                i -= 1
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play(1)
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_RALT:
                pygame.mixer.music.unpause()
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:
        #         pygame.mixer.music.unpause()
        pygame.mixer.music.queue(playlist[(i + 1) % len(playlist)])

    pygame.display.flip()
pygame.quit()
    