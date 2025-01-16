import pygame
import sys

# Ensure UTF-8 encoding
def main():
    # Initialize pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Paddle dimensions
    PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
    BALL_SIZE = 10

    # Speeds
    PADDLE_SPEED = 7
    BALL_SPEED = 5

    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    # Clock to control frame rate
    clock = pygame.time.Clock()

    # Initialize paddle and ball positions
    left_paddle = pygame.Rect(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 20, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

    # Ball direction
    ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

    # Scores
    left_score, right_score = 0, 0

    # Font for score display
    font = pygame.font.Font(None, 74)

    def reset_ball():
        nonlocal ball_dx, ball_dy
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get keys
        keys = pygame.key.get_pressed()

        # Move left paddle
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED

        # Move right paddle
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Move the ball
        ball.x += ball_dx
        ball.y += ball_dy

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_dx *= -1

        # Ball out of bounds
        if ball.left <= 0:
            right_score += 1
            reset_ball()
        if ball.right >= WIDTH:
            left_score += 1
            reset_ball()

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Display scores
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (WIDTH // 4, 20))
        screen.blit(right_text, (WIDTH - WIDTH // 4 - 50, 20))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)
        
        