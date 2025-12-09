# API Reference

## Module: src.config

### Class: Config

Central configuration class containing all game settings.

#### Class Attributes

##### Screen & Grid
- `SCREEN_WIDTH: int = 800` - Total screen width in pixels
- `SCREEN_HEIGHT: int = 600` - Total screen height in pixels
- `BLOCK_SIZE: int = 30` - Size of each grid block in pixels
- `GAME_WIDTH: int = 300` - Width of the game play area
- `COLUMNS: int = 10` - Number of columns in the game grid
- `ROWS: int` - Number of rows in the game grid (calculated)
- `FPS: int = 60` - Target frames per second

##### Colors (RGB tuples)
- `WHITE: tuple = (255, 255, 255)`
- `BLACK: tuple = (0, 0, 0)`
- `GRAY: tuple = (128, 128, 128)`
- `DARK_GRAY: tuple = (50, 50, 50)`
- `LIGHT_GRAY: tuple = (200, 200, 200)`
- `RED: tuple = (255, 0, 0)`
- `GREEN: tuple = (0, 255, 0)`
- `BLUE: tuple = (0, 0, 255)`
- `YELLOW: tuple = (255, 255, 0)`
- `CYAN: tuple = (0, 255, 255)`
- `MAGENTA: tuple = (255, 0, 255)`
- `ORANGE: tuple = (255, 165, 0)`
- `PURPLE: tuple = (128, 0, 128)`
- `COLORS: list` - List of available tetromino colors

##### Fonts
- `FONT_SMALL: pygame.font.Font` - 24pt font
- `FONT_MEDIUM: pygame.font.Font` - 36pt font
- `FONT_LARGE: pygame.font.Font` - 48pt font
- `FONT_HUGE: pygame.font.Font` - 72pt font

##### Game Mechanics
- `SHAPES: list` - List of 2D arrays defining tetromino shapes
- `SHAPE_NAMES: dict` - Mapping of shape indices to names
- `INITIAL_FALL_SPEED: int = 500` - Initial fall speed in milliseconds
- `MIN_FALL_SPEED: int = 100` - Maximum speed (minimum time)
- `SPEED_INCREMENT: int = 50` - Speed increase per level
- `POINTS_PER_LEVEL: int = 100` - Points needed per level
- `POINTS_PER_ROW: int = 100` - Base points per row cleared
- `COMBO_MULTIPLIER: dict` - Score multipliers for line clears

##### Game States
- `STATE_MENU: str = "menu"`
- `STATE_LOGIN: str = "login"`
- `STATE_PLAYING: str = "playing"`
- `STATE_PAUSED: str = "paused"`
- `STATE_GAME_OVER: str = "game_over"`

##### Controls
- `CONTROLS: dict` - Mapping of actions to key descriptions

#### Methods

##### get_level_speed(level: int) -> int
Calculate fall speed for a given level.

**Parameters:**
- `level` (int): Current game level

**Returns:**
- `int`: Fall speed in milliseconds

**Example:**
```python
speed = Config.get_level_speed(5)  # Returns 250
```

##### calculate_score(rows_cleared: int) -> int
Calculate score based on rows cleared.

**Parameters:**
- `rows_cleared` (int): Number of rows cleared simultaneously

**Returns:**
- `int`: Points earned

**Example:**
```python
score = Config.calculate_score(4)  # Tetris! Returns 1000
```

---

## Module: src.tetromino

### Class: Tetromino

Represents a single game piece.

#### Attributes
- `shape: list[list[int]]` - 2D array representing block pattern
- `color: tuple` - RGB color value
- `x: int` - Horizontal position on grid
- `y: int` - Vertical position on grid
- `shape_type: int` - Index in Config.SHAPES

#### Methods

##### \_\_init\_\_(shape_type: int = None)
Create a new tetromino.

**Parameters:**
- `shape_type` (int, optional): Specific shape index. Random if None.

**Example:**
```python
piece = Tetromino()  # Random piece
i_block = Tetromino(0)  # Create I-block
```

##### rotate_clockwise() -> None
Rotate the piece 90° clockwise.

**Example:**
```python
piece.rotate_clockwise()
```

##### rotate_counterclockwise() -> None
Rotate the piece 90° counterclockwise.

##### get_blocks() -> list[tuple[int, int]]
Get absolute positions of all blocks.

**Returns:**
- `list`: List of (x, y) coordinate tuples

**Example:**
```python
blocks = piece.get_blocks()
# [(5, 3), (6, 3), (7, 3), (8, 3)]
```

##### get_width() -> int
Get width of the piece.

**Returns:**
- `int`: Width in blocks

##### get_height() -> int
Get height of the piece.

**Returns:**
- `int`: Height in blocks

##### clone() -> Tetromino
Create a copy of this piece.

**Returns:**
- `Tetromino`: New instance with same properties

---

## Module: src.grid

### Class: Grid

Manages the game board.

#### Attributes
- `grid: list[list]` - 2D array representing board state
- `rows: int` - Number of rows
- `cols: int` - Number of columns

#### Methods

##### \_\_init\_\_()
Initialize empty grid.

**Example:**
```python
grid = Grid()
```

##### is_valid_position(tetromino: Tetromino, offset_x: int = 0, offset_y: int = 0) -> bool
Check if piece can be placed at position.

**Parameters:**
- `tetromino` (Tetromino): Piece to check
- `offset_x` (int): Horizontal offset from current position
- `offset_y` (int): Vertical offset from current position

**Returns:**
- `bool`: True if valid, False otherwise

**Example:**
```python
if grid.is_valid_position(piece, 1, 0):
    piece.x += 1  # Move right
```

##### lock_tetromino(tetromino: Tetromino) -> None
Lock piece into the grid permanently.

**Parameters:**
- `tetromino` (Tetromino): Piece to lock

##### clear_full_rows() -> int
Clear all complete rows.

**Returns:**
- `int`: Number of rows cleared

**Example:**
```python
rows = grid.clear_full_rows()
score += Config.calculate_score(rows)
```

##### is_game_over() -> bool
Check if game is over.

**Returns:**
- `bool`: True if top row has blocks

##### get_filled_cells() -> list[tuple]
Get all filled cell positions and colors.

**Returns:**
- `list`: List of ((x, y), color) tuples

##### clear() -> None
Reset grid to empty state.

##### get_height() -> int
Get current stack height.

**Returns:**
- `int`: Number of rows from bottom containing blocks

---

## Module: src.ui

### Class: UI

Manages user interface rendering.

#### Attributes
- `screen: pygame.Surface` - Display surface
- `clock: pygame.time.Clock` - Game clock

#### Methods

##### \_\_init\_\_(screen: pygame.Surface, clock: pygame.time.Clock)
Initialize UI manager.

**Parameters:**
- `screen`: Pygame display surface
- `clock`: Game clock

##### draw_welcome_screen() -> bool
Display welcome screen.

**Returns:**
- `bool`: True to start game, False to quit

##### draw_login_screen() -> str
Display login screen.

**Returns:**
- `str`: Player name entered

##### draw_game_header(player_name: str, score: int, level: int, high_score: int) -> None
Draw header bar.

**Parameters:**
- `player_name` (str): Player's name
- `score` (int): Current score
- `level` (int): Current level
- `high_score` (int): High score

##### draw_sidebar(next_tetromino: Tetromino, lines_cleared: int, controls_visible: bool = True) -> None
Draw sidebar with info.

**Parameters:**
- `next_tetromino` (Tetromino): Next piece to display
- `lines_cleared` (int): Total lines cleared
- `controls_visible` (bool): Whether to show controls

##### draw_game_over_screen(score: int, high_score: int) -> str
Display game over screen.

**Parameters:**
- `score` (int): Final score
- `high_score` (int): High score

**Returns:**
- `str`: "restart" or "quit"

##### draw_pause_screen() -> None
Draw pause overlay.

---

## Module: src.game

### Class: TetrisGame

Main game controller.

#### Attributes
- `screen: pygame.Surface` - Display surface
- `clock: pygame.time.Clock` - Game clock
- `grid: Grid` - Game board
- `ui: UI` - UI manager
- `current_piece: Tetromino` - Falling piece
- `next_piece: Tetromino` - Next piece
- `state: str` - Current game state
- `score: int` - Current score
- `level: int` - Current level
- `lines_cleared: int` - Total lines cleared
- `high_score: int` - High score
- `player_name: str` - Player's name
- `paused: bool` - Whether game is paused

#### Methods

##### \_\_init\_\_()
Initialize game.

**Example:**
```python
game = TetrisGame()
```

##### reset_game() -> None
Reset game state for new game.

##### handle_input() -> None
Process user input events.

##### lock_current_piece() -> None
Lock current piece and spawn next.

##### update() -> None
Update game state.

##### draw_grid() -> None
Draw game grid and placed blocks.

##### draw_current_piece() -> None
Draw falling piece.

##### draw_ghost_piece() -> None
Draw ghost piece preview.

##### render() -> None
Render all game elements.

##### run_menu() -> None
Run menu state.

##### run_login() -> None
Run login state.

##### run_playing() -> None
Run main game loop.

##### run_game_over() -> None
Run game over state.

##### run() -> None
Main game loop entry point.

**Example:**
```python
game = TetrisGame()
game.run()  # Start the game
```

##### quit_game() -> None
Quit game cleanly.

---

## Usage Examples

### Basic Game Launch
```python
from src.game import TetrisGame

game = TetrisGame()
game.run()
```

### Custom Configuration
```python
from src.config import Config

# Modify settings
Config.SCREEN_WIDTH = 1024
Config.INITIAL_FALL_SPEED = 300

from src.game import TetrisGame
game = TetrisGame()
game.run()
```

### Manual Game Control
```python
from src.game import TetrisGame

game = TetrisGame()

# Manual state management
game.state = Config.STATE_PLAYING
game.reset_game()

# Custom game loop
while True:
    game.handle_input()
    game.update()
    game.render()
    game.clock.tick(60)
```

### Testing Components
```python
from src.tetromino import Tetromino
from src.grid import Grid

# Create test pieces
grid = Grid()
piece = Tetromino(0)  # I-block

# Test collision
print(grid.is_valid_position(piece))  # True

# Test rotation
piece.rotate_clockwise()
print(f"Width: {piece.get_width()}, Height: {piece.get_height()}")
```

---

## Event Handling

### Keyboard Events

| Event | Key | Action |
|-------|-----|--------|
| Move Left | `pygame.K_LEFT` | Move piece left |
| Move Right | `pygame.K_RIGHT` | Move piece right |
| Soft Drop | `pygame.K_DOWN` | Move piece down |
| Rotate | `pygame.K_UP` | Rotate clockwise |
| Hard Drop | `pygame.K_SPACE` | Drop to bottom |
| Pause | `pygame.K_p` | Toggle pause |
| Quit | `pygame.K_ESCAPE` | Return to menu |

### Custom Event Handling
```python
def custom_handle_input(self):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                # Custom action
                self.save_game()
```

---

## Error Handling

### Common Exceptions

```python
try:
    game = TetrisGame()
    game.run()
except ImportError:
    print("Pygame not installed: pip install pygame")
except pygame.error as e:
    print(f"Pygame error: {e}")
except KeyboardInterrupt:
    print("Game interrupted by user")
```

---

## Performance Tips

1. **Minimize redraws**: Only redraw changed areas
2. **Use dirty rect updates**: `pygame.display.update(rect_list)`
3. **Optimize collision checks**: Check only piece blocks
4. **Cache surfaces**: Store rendered text surfaces
5. **Profile code**: Use `cProfile` to find bottlenecks

---

## Extension Points

### Adding New Features

```python
class ExtendedTetrisGame(TetrisGame):
    def __init__(self):
        super().__init__()
        self.held_piece = None
    
    def hold_piece(self):
        if self.held_piece is None:
            self.held_piece = self.current_piece
            self.current_piece = self.next_piece
            self.next_piece = Tetromino()
        else:
            self.current_piece, self.held_piece = \
                self.held_piece, self.current_piece
```

---

## Version History

- **v1.0.0** (2025) - Initial release
  - Complete game implementation
  - Full documentation
  - Educational features

---

## License

MIT License - See LICENSE file for details
