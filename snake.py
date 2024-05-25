import pygame 
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake parameters
snake_size = 20
snake_speed = 5
snake_x, snake_y = width // 2, height // 2
snake_dx, snake_dy = snake_size, 0
snake_segments = [(snake_x, snake_y)]

# Food parameters
food_size = 20
food_x, food_y = random.randint(0, (width - food_size) // 20) * 20, random.randint(0, (height - food_size) // 20) * 20

# Score variable
score = 0

def restart_game():
    global snake_x, snake_y, snake_dx, snake_dy, snake_segments, food_x, food_y, score, game_over
    snake_x, snake_y = width // 2, height // 2
    snake_dx, snake_dy = snake_size, 0
    snake_segments = [(snake_x, snake_y)]
    food_x, food_y = random.randint(0, (width - food_size) // 20) * 20, random.randint(0, (height - food_size) // 20) * 20
    score = 0
    game_over = False

# Main game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy == 0:
                snake_dy = -snake_size
                snake_dx = 0
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dy = snake_size
                snake_dx = 0
            elif event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -snake_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = snake_size
                snake_dy = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if restart_button_rect.collidepoint(event.pos):
                restart_game()



    # Move the snake
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if snake eats the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        print("Yummy! Score:", score)
        snake_segments.append((snake_x, snake_y))
        food_x, food_y = random.randint(0, (width - food_size) // 20) * 20, random.randint(0, (height - food_size) // 20) * 20

    # Add new segment to the front of the snake
    snake_segments.insert(0, (snake_x, snake_y))
    if snake_x != food_x or snake_y != food_y:
        # Remove the last segment if the snake hasn't eaten food
        snake_segments.pop()

    # Check if snake hits the boundary
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        game_over = True
    elif (snake_x,snake_y) in snake_segments[1:]:
        game_over = True    
    # Draw everything on the screen
    screen.fill(BLACK)
    if not game_over:
        for segment in snake_segments:
            pygame.draw.circle(screen, GREEN, segment, snake_size // 2)
        pygame.draw.rect(screen, WHITE, (food_x, food_y, food_size, food_size))
    else:
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Game Over", True, RED)
        game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, game_over_rect)


        # Draw restart button
        restart_button_rect = pygame.Rect(width // 2 - 50, height // 2 + 50, 100, 40)
        pygame.draw.rect(screen, GREEN, restart_button_rect)
        font = pygame.font.Font(None, 24)
        restart_text = font.render("Restart", True, BLACK)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        screen.blit(restart_text, restart_text_rect)

    # Display score in the top right corner
    font = pygame.font.Font(None, 36)    
    score_text = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_text.get_rect(topright=(width - 10, 10))
    screen.blit(score_text, score_rect)

    # Update the display
    pygame.display.update()

    # Limit frame rate
    pygame.time.Clock().tick(snake_speed)

pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
sys.exit()
