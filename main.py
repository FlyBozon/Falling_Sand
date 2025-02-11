import pygame
import random

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 5
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
SAND_COLOR = (194, 178, 128)
BACKGROUND_COLOR = (0, 0, 0)

grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Sand Simulation")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            grid[my // GRID_SIZE][mx // GRID_SIZE] = SAND_COLOR
    
    # Update sand particles
    for y in range(ROWS - 2, -1, -1):  # Start from bottom row upwards
        for x in range(COLS):
            if grid[y][x] == SAND_COLOR:
                if grid[y + 1][x] is None:  # Fall straight down
                    grid[y + 1][x] = SAND_COLOR
                    grid[y][x] = None
                elif x > 0 and grid[y + 1][x - 1] is None:  # Fall left
                    grid[y + 1][x - 1] = SAND_COLOR
                    grid[y][x] = None
                elif x < COLS - 1 and grid[y + 1][x + 1] is None:  # Fall right
                    grid[y + 1][x + 1] = SAND_COLOR
                    grid[y][x] = None
    
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] is not None:
                pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
