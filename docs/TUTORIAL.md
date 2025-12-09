# Python Tetris Game - Tutorial

## Step-by-Step Development Guide

This tutorial explains how the Tetris game was built, teaching you game development concepts along the way.

## Table of Contents

1. [Project Setup](#1-project-setup)
2. [Configuration System](#2-configuration-system)
3. [Game Entities](#3-game-entities)
4. [Grid Management](#4-grid-management)
5. [User Interface](#5-user-interface)
6. [Game Loop](#6-game-loop)
7. [Testing & Debugging](#7-testing--debugging)
8. [Enhancements](#8-enhancements)

---

## 1. Project Setup

### Step 1.1: Install Python and Pygame

```bash
# Check Python version (need 3.7+)
python --version

# Install Pygame
pip install pygame
```

### Step 1.2: Create Project Structure

```
Python-Tetris-Game-/
├── main.py           # Entry point
├── src/              # Source code
│   ├── __init__.py
│   ├── config.py     # Constants
│   ├── tetromino.py  # Game pieces
│   ├── grid.py       # Game board
│   ├── ui.py         # User interface
│   └── game.py       # Main logic
└── requirements.txt  # Dependencies
```

### Step 1.3: Basic Pygame Template

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Learning Points:**
- Pygame initialization
- Event loop
- Frame rate control

---

## 2. Configuration System

### Why Use a Config File?

Instead of hardcoding values throughout your code:
```python
# BAD - Magic numbers everywhere
screen = pygame.display.set_mode((800, 600))
speed = 500
```

Use a centralized configuration:
```python
# GOOD - Clear and maintainable
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
speed = Config.INITIAL_FALL_SPEED
```

### Creating config.py

```python
class Config:
    # Screen settings
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BLOCK_SIZE = 30
    
    # Colors (RGB tuples)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    # Game mechanics
    FPS = 60
    INITIAL_FALL_SPEED = 500  # milliseconds
```

**Learning Points:**
- Separation of data and logic
- Easy to modify game behavior
- No duplicate values

---

## 3. Game Entities

### Understanding Tetrominoes

A tetromino is represented as a 2D list:
```python
# I-shape
[
    [1, 1, 1, 1]
]

# L-shape
[
    [1, 0, 0],
    [1, 1, 1]
]
```

Where `1` = filled block, `0` = empty space.

### Creating the Tetromino Class

```python
class Tetromino:
    def __init__(self):
        # Choose random shape and color
        self.shape = random.choice(Config.SHAPES)
        self.color = random.choice(Config.COLORS)
        
        # Start at top center
        self.x = Config.COLUMNS // 2
        self.y = 0
```

### Rotation Algorithm

To rotate a matrix 90° clockwise:
1. Transpose (swap rows and columns)
2. Reverse each row

```python
def rotate_clockwise(self):
    # Transpose
    transposed = zip(*self.shape[::-1])
    # Convert to lists
    self.shape = [list(row) for row in transposed]
```

**Visual Example:**
```
Before:        After:
[1, 0]        [1, 1]
[1, 1]  -->   [0, 1]
```

**Learning Points:**
- Matrix operations
- List comprehensions
- Algorithm implementation

---

## 4. Grid Management

### Grid Structure

The game board is a 2D list:
```python
# 0 = empty, color tuple = filled
grid = [
    [0, 0, 0, (255,0,0), 0],  # Row 0
    [0, 0, 0, 0, 0],           # Row 1
    # ... more rows
]
```

### Collision Detection

Check if piece can move to new position:
```python
def is_valid_position(self, tetromino, offset_x=0, offset_y=0):
    for row_idx, row in enumerate(tetromino.shape):
        for col_idx, cell in enumerate(row):
            if cell:  # If filled block
                new_x = tetromino.x + col_idx + offset_x
                new_y = tetromino.y + row_idx + offset_y
                
                # Check boundaries
                if new_x < 0 or new_x >= self.cols:
                    return False
                if new_y >= self.rows:
                    return False
                
                # Check collision with other pieces
                if new_y >= 0 and self.grid[new_y][new_x]:
                    return False
    
    return True
```

### Line Clearing

Remove full rows:
```python
def clear_full_rows(self):
    rows_cleared = 0
    row_idx = self.rows - 1
    
    while row_idx >= 0:
        if all(self.grid[row_idx]):  # Row is full
            del self.grid[row_idx]
            self.grid.insert(0, [0] * self.cols)
            rows_cleared += 1
        else:
            row_idx -= 1
    
    return rows_cleared
```

**Learning Points:**
- 2D array manipulation
- Boundary checking
- List operations

---

## 5. User Interface

### Drawing the Grid

```python
def draw_grid(self):
    for y in range(Config.ROWS):
        for x in range(Config.COLUMNS):
            if self.grid[y][x]:  # If cell is filled
                color = self.grid[y][x]
                pygame.draw.rect(
                    self.screen, color,
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, 
                     BLOCK_SIZE, BLOCK_SIZE)
                )
```

### Drawing Tetrominoes

```python
def draw_current_piece(self):
    for row_idx, row in enumerate(self.current_piece.shape):
        for col_idx, cell in enumerate(row):
            if cell:
                x = (self.current_piece.x + col_idx) * BLOCK_SIZE
                y = (self.current_piece.y + row_idx) * BLOCK_SIZE
                
                pygame.draw.rect(
                    self.screen, self.current_piece.color,
                    (x, y, BLOCK_SIZE, BLOCK_SIZE)
                )
```

### Text Rendering

```python
score_text = font.render(f"Score: {score}", True, WHITE)
screen.blit(score_text, (10, 10))
```

**Learning Points:**
- Pygame drawing functions
- Coordinate systems
- Screen rendering

---

## 6. Game Loop

### The Main Loop Structure

```python
def run(self):
    running = True
    while running:
        # 1. Handle Input
        self.handle_input()
        
        # 2. Update Game State
        self.update()
        
        # 3. Render Graphics
        self.render()
        
        # 4. Control Frame Rate
        self.clock.tick(Config.FPS)
```

### Input Handling

```python
def handle_input(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.quit_game()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.grid.is_valid_position(self.current_piece, -1, 0):
                    self.current_piece.x -= 1
            
            if event.key == pygame.K_UP:
                self.current_piece.rotate_clockwise()
                if not self.grid.is_valid_position(self.current_piece):
                    self.current_piece.rotate_counterclockwise()
```

### Update Logic

```python
def update(self):
    self.fall_time += self.clock.get_rawtime()
    
    if self.fall_time >= self.fall_speed:
        self.fall_time = 0
        
        if self.grid.is_valid_position(self.current_piece, 0, 1):
            self.current_piece.y += 1
        else:
            self.lock_current_piece()
```

### State Management

```python
class GameState:
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"

# In game loop
if self.state == GameState.PLAYING:
    self.run_playing()
elif self.state == GameState.PAUSED:
    self.run_paused()
```

**Learning Points:**
- Game loop architecture
- Event-driven programming
- State machines
- Timing and updates

---

## 7. Testing & Debugging

### Print Debugging

```python
# Debug piece position
print(f"Piece at ({self.current_piece.x}, {self.current_piece.y})")

# Debug grid state
print('\n'.join([''.join(['█' if cell else '·' for cell in row]) 
                 for row in self.grid]))
```

### Common Issues

**Issue: Piece falls too fast**
```python
# Solution: Check fall_speed value
print(f"Fall speed: {self.fall_speed}ms")
```

**Issue: Collision not working**
```python
# Solution: Add logging
def is_valid_position(self, ...):
    result = # ... calculation
    print(f"Collision check: {result}")
    return result
```

**Issue: Rotation causes crash**
```python
# Solution: Defensive programming
try:
    self.current_piece.rotate_clockwise()
except IndexError as e:
    print(f"Rotation error: {e}")
    # Revert rotation
```

---

## 8. Enhancements

### Adding Sound Effects

```python
import pygame.mixer

# Load sounds
pygame.mixer.init()
drop_sound = pygame.mixer.Sound('assets/sounds/drop.wav')
clear_sound = pygame.mixer.Sound('assets/sounds/clear.wav')

# Play sounds
drop_sound.play()
```

### Adding Particle Effects

```python
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.velocity_y = -5
        self.color = color
        self.lifetime = 30
    
    def update(self):
        self.y += self.velocity_y
        self.velocity_y += 0.5  # Gravity
        self.lifetime -= 1
    
    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, 
                             (int(self.x), int(self.y)), 3)
```

### Implementing Hold Feature

```python
def hold_piece(self):
    if not self.hold_used:
        if self.held_piece is None:
            self.held_piece = self.current_piece
            self.current_piece = self.next_piece
            self.next_piece = Tetromino()
        else:
            self.current_piece, self.held_piece = \
                self.held_piece, self.current_piece
        
        self.hold_used = True
```

---

## Practice Exercises

### Beginner
1. Change the game colors
2. Modify the grid size
3. Add a pause screen
4. Display lines cleared

### Intermediate
5. Implement a high score save system
6. Add difficulty levels
7. Create custom piece shapes
8. Add background music

### Advanced
9. Implement T-spin detection
10. Add network multiplayer
11. Create an AI player
12. Build a level editor

---

## Resources

### Documentation
- [Pygame Docs](https://www.pygame.org/docs/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Learning
- [Game Programming Patterns](https://gameprogrammingpatterns.com/)
- [Pygame Tutorials](https://www.pygame.org/wiki/tutorials)

### Community
- [r/pygame](https://reddit.com/r/pygame)
- [Pygame Discord](https://discord.gg/pygame)

---

## Next Steps

1. **Complete the tutorial** - Build the game step by step
2. **Modify the code** - Change colors, speeds, scoring
3. **Add features** - Implement enhancements from section 8
4. **Share your work** - Post on GitHub, get feedback
5. **Learn more** - Try building other games

Happy coding! 🎮
