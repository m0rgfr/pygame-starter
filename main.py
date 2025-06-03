import pygame


class Boss:
    """Simple boss that moves horizontally across the screen."""

    def __init__(self, x: int, y: int, width: int = 60, height: int = 40):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 50, 50)
        self.direction = 1

    def update(self, screen_width: int) -> None:
        """Move the boss and bounce at screen edges."""
        self.rect.x += 3 * self.direction
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction *= -1

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Starter")

# Create a boss instance
boss = Boss(290, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    boss.update(screen.get_width())
    boss.draw(screen)
    pygame.display.flip()

pygame.quit()
