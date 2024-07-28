import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Ball dimensions
BALL_SIZE = 20

# Paddle speed
PADDLE_SPEED = 6

# Ball speed
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, y_change):
        self.rect.y += y_change
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.x_speed = BALL_SPEED_X * random.choice((1, -1))
        self.y_speed = BALL_SPEED_Y * random.choice((1, -1))

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ball collision with top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.y_speed = -self.y_speed

        # Ball collision with paddles
        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(right_paddle.rect):
            self.x_speed = -self.x_speed

        # Ball out of bounds
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.x_speed = BALL_SPEED_X * random.choice((1, -1))
            self.y_speed = BALL_SPEED_Y * random.choice((1, -1))

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

# Create paddles and ball
left_paddle = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(SCREEN_WIDTH - 30 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_s]:
        left_paddle.move(PADDLE_SPEED)
    if keys[pygame.K_UP]:
        right_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        right_paddle.move(PADDLE_SPEED)

    ball.move()

    screen.fill(BLACK)
    left_paddle.draw()
    right_paddle.draw()
    ball.draw()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()