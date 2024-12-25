import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen and Game Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600  # Reduced height
BLOCK_SIZE = 30
COLUMNS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = (SCREEN_HEIGHT - 100) // BLOCK_SIZE  # Deduct space for the header
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (50, 50, 50)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE]

# Fonts
FONT = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 36)
HUGE_FONT = pygame.font.Font(None, 48)

# Tetromino Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 0, 0], [1, 1, 1]],  # L shape
    [[0, 0, 1], [1, 1, 1]],  # J shape,
]

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Tetromino Class
class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def draw_welcome_screen():
    """Display the welcome screen."""
    running = True
    while running:
        screen.fill(BLACK)

        # Title text
        title_text = HUGE_FONT.render("Tetris", True, CYAN)
        screen.blit(
            title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 150)
        )

        # Instruction text
        instruction_text = FONT.render("Press ENTER to Start", True, WHITE)
        screen.blit(
            instruction_text,
            (
                SCREEN_WIDTH // 2 - instruction_text.get_width() // 2,
                250,
            ),
        )

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

def collision(tetromino, grid, offset_x, offset_y):
    for row_index, row in enumerate(tetromino.shape):
        for col_index, cell in enumerate(row):
            if cell:
                new_x = tetromino.x + col_index + offset_x
                new_y = tetromino.y + row_index + offset_y
                if (
                    new_x < 0
                    or new_x >= COLUMNS
                    or new_y >= ROWS
                    or (new_y >= 0 and grid[new_y][new_x])
                ):
                    return True
    return False

def clear_rows(grid):
    rows_cleared = 0
    for row_index in range(ROWS):
        if all(grid[row_index]):
            del grid[row_index]
            grid.insert(0, [0] * COLUMNS)
            rows_cleared += 1
    return rows_cleared

def draw_grid(grid):
    for y in range(ROWS):
        for x in range(COLUMNS):
            if grid[y][x]:
                pygame.draw.rect(
                    screen,
                    grid[y][x],
                    (x * BLOCK_SIZE, y * BLOCK_SIZE + 100, BLOCK_SIZE, BLOCK_SIZE),
                )
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (x * BLOCK_SIZE, y * BLOCK_SIZE + 100, BLOCK_SIZE, BLOCK_SIZE),
                    1,
                )

def draw_tetromino(tetromino):
    for row_index, row in enumerate(tetromino.shape):
        for col_index, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    tetromino.color,
                    (
                        (tetromino.x + col_index) * BLOCK_SIZE,
                        (tetromino.y + row_index) * BLOCK_SIZE + 100,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                )
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (
                        (tetromino.x + col_index) * BLOCK_SIZE,
                        (tetromino.y + row_index) * BLOCK_SIZE + 100,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                    1,
                )

def draw_header(player_name, score, high_score):
    pygame.draw.rect(screen, GREEN, (0, 0, SCREEN_WIDTH, 50))
    title_text = LARGE_FONT.render("Tetris", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 10))
    name_text = FONT.render(f"Player: {player_name}", True, WHITE)
    screen.blit(name_text, (10, 60))
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 80))
    high_score_text = FONT.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(high_score_text, (SCREEN_WIDTH - high_score_text.get_width() - 10, 80))

def login_page():
    input_box = pygame.Rect(50, SCREEN_HEIGHT // 2 - 20, 200, 40)
    color_inactive = GRAY
    color_active = WHITE
    color = color_inactive
    active = False
    text = ""
    running = True

    while running:
        screen.fill(BLACK)
        prompt = FONT.render("Enter your name:", True, WHITE)
        screen.blit(prompt, (50, SCREEN_HEIGHT // 2 - 80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = FONT.render(text, True, WHITE)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()
        clock.tick(FPS)

def main():
    draw_welcome_screen()
    player_name = login_page()

    grid = [[0] * COLUMNS for _ in range(ROWS)]
    current_tetromino = Tetromino()
    next_tetromino = Tetromino()
    score = 0
    high_score = 0
    fall_speed = 500
    fall_time = 0

    running = True
    while running:
        fall_time += clock.get_rawtime()
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not collision(
                    current_tetromino, grid, -1, 0
                ):
                    current_tetromino.x -= 1
                if event.key == pygame.K_RIGHT and not collision(
                    current_tetromino, grid, 1, 0
                ):
                    current_tetromino.x += 1
                if event.key == pygame.K_DOWN and not collision(
                    current_tetromino, grid, 0, 1
                ):
                    current_tetromino.y += 1
                if event.key == pygame.K_UP:
                    current_tetromino.rotate()
                    if collision(current_tetromino, grid, 0, 0):
                        current_tetromino.rotate()

        if fall_time >= fall_speed:
            fall_time = 0
            if not collision(current_tetromino, grid, 0, 1):
                current_tetromino.y += 1
            else:
                for row_index, row in enumerate(current_tetromino.shape):
                    for col_index, cell in enumerate(row):
                        if cell:
                            grid[current_tetromino.y + row_index][
                                current_tetromino.x + col_index
                            ] = current_tetromino.color
                score += clear_rows(grid) * 10
                if score > high_score:
                    high_score = score

                # Speed adjustment logic
                if score > 0 and score % 50 == 0:  # Speed up every 50 points
                    fall_speed = max(100, 500 - (score // 50) * 50)  # Minimum speed is 100 ms

                current_tetromino = next_tetromino
                next_tetromino = Tetromino()
                if collision(current_tetromino, grid, 0, 0):
                    running = False

        draw_header(player_name, score, high_score)
        draw_grid(grid)
        draw_tetromino(current_tetromino)
        pygame.display.flip()

                                pygame.quit()

if __name__ == "__main__":
    main()
