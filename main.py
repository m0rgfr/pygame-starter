import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Starter")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()
