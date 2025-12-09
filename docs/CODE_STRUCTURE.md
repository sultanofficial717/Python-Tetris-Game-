# Code Structure and Architecture

## Overview
This document explains the architectural decisions, design patterns, and code organization of the Python Tetris game.

## Architecture Pattern

### Model-View-Controller (MVC) Inspired
The project uses a modified MVC pattern adapted for game development:

```
┌─────────────────────────────────────┐
│           Game (Controller)          │
│  - Orchestrates all components      │
│  - Manages game loop                │
│  - Handles input                    │
└──────────┬─────────────┬────────────┘
           │             │
     ┌─────▼─────┐  ┌───▼────────┐
     │ Model     │  │ View (UI)  │
     │ - Grid    │  │ - Render   │
     │ - Tetro   │  │ - Screens  │
     └───────────┘  └────────────┘
```

## Module Organization

### 1. config.py - Configuration Layer
**Purpose**: Centralize all game constants and settings

**Key Components**:
- Screen dimensions
- Color definitions
- Shape templates
- Game mechanics settings
- Scoring rules

**Design Benefits**:
- Easy to modify game behavior
- No magic numbers in code
- Single source of truth
- Enables A/B testing

**Example**:
```python
class Config:
    SCREEN_WIDTH = 800
    COLUMNS = 10
    COLORS = [RED, GREEN, BLUE, ...]
```

### 2. tetromino.py - Game Entity
**Purpose**: Represent individual game pieces

**Responsibilities**:
- Store piece shape and color
- Handle rotation transformations
- Track position on grid
- Provide block coordinates

**OOP Concepts**:
- Encapsulation: Internal state hidden
- Abstraction: Simple public interface
- Methods: Behaviors attached to data

**Key Methods**:
```python
- __init__(): Create new piece
- rotate_clockwise(): Transform shape
- get_blocks(): Return absolute positions
- clone(): Create copy for preview
```

### 3. grid.py - Game State Manager
**Purpose**: Manage the game board and collision logic

**Responsibilities**:
- Store locked pieces
- Validate piece positions
- Clear completed rows
- Check game over condition

**Data Structure**:
```python
grid = [
    [0, 0, 0, color, 0, ...],  # Row 0 (top)
    [0, color, color, 0, ...],  # Row 1
    ...
]
# 0 = empty cell
# color tuple = filled cell
```

**Algorithm Highlights**:
- Collision detection: O(blocks) time
- Row clearing: O(rows) time
- Space complexity: O(rows × cols)

### 4. ui.py - Presentation Layer
**Purpose**: Handle all user interface rendering

**Responsibilities**:
- Draw game screens
- Render game elements
- Handle visual effects
- Manage user prompts

**Separation of Concerns**:
- UI logic separate from game logic
- Easy to modify visuals without breaking mechanics
- Could swap to different rendering engine

**Screen Components**:
- Welcome screen
- Login screen
- Game header
- Sidebar
- Game over screen
- Pause overlay

### 5. game.py - Game Controller
**Purpose**: Orchestrate all components and manage game flow

**Responsibilities**:
- Run game loop
- Process input events
- Update game state
- Coordinate rendering
- Manage state transitions

**Game Loop Pattern**:
```python
while running:
    handle_input()    # Process events
    update()          # Update state
    render()          # Draw frame
    clock.tick(FPS)   # Maintain frame rate
```

**State Machine**:
```
MENU → LOGIN → PLAYING ⇄ PAUSED → GAME_OVER → MENU
```

## Design Patterns Used

### 1. Singleton Pattern (Implicit)
**Where**: Config class
**Why**: Single source of truth for settings
**Implementation**: Class-level variables

### 2. Factory Pattern (Implicit)
**Where**: Tetromino creation
**Why**: Centralize piece generation logic
**Implementation**: `__init__` with random selection

### 3. State Pattern
**Where**: Game states (menu, playing, paused, etc.)
**Why**: Clean state management and transitions
**Implementation**: State variable with dedicated methods

### 4. Strategy Pattern (Future)
**Where**: Different difficulty modes
**Why**: Easily switch game behavior
**Implementation**: Configurable speed/scoring functions

## Data Flow

### Initialization Flow
```
1. Initialize Pygame
2. Create screen surface
3. Load Config settings
4. Initialize Grid
5. Initialize UI
6. Enter menu state
```

### Game Loop Flow
```
┌─ While Running ─────────────────┐
│                                  │
│  ┌── Handle Input              │
│  │   - Keyboard events          │
│  │   - Quit detection           │
│  │                              │
│  ┌── Update State               │
│  │   - Fall timer               │
│  │   - Piece movement           │
│  │   - Collision check          │
│  │   - Lock pieces              │
│  │   - Clear rows               │
│  │   - Update score             │
│  │                              │
│  ┌── Render                     │
│  │   - Clear screen             │
│  │   - Draw grid                │
│  │   - Draw pieces              │
│  │   - Draw UI                  │
│  │   - Flip display             │
│  │                              │
│  └── Tick Clock (60 FPS)        │
│                                  │
└──────────────────────────────────┘
```

### Input Processing Flow
```
Event → Game.handle_input() → Validate → Update Piece Position
                                      → Collision? → Undo Movement
```

## Error Handling

### Defensive Programming
- Input validation before state changes
- Boundary checks for grid access
- Collision checks before movement
- Safe array indexing

### Graceful Degradation
- Invalid moves are ignored, not crashed
- Rotation reverts if invalid
- Game continues even with unexpected input

## Performance Considerations

### Optimization Strategies
1. **Minimal Redraws**: Only draw when state changes
2. **Efficient Collision**: Check only piece blocks, not entire grid
3. **Simple Data Structures**: Lists and tuples for speed
4. **Frame Limiting**: Consistent 60 FPS prevents CPU waste

### Complexity Analysis
- Piece movement: O(1)
- Collision detection: O(blocks) ≈ O(4) = O(1)
- Row clearing: O(rows) = O(20) = O(1)
- Rendering: O(rows × cols) = O(200) = O(1)

Overall: All operations are effectively O(1) for game context.

## Extensibility

### Easy to Add
- ✅ New piece shapes (add to Config.SHAPES)
- ✅ New colors (add to Config.COLORS)
- ✅ Sound effects (add sound module)
- ✅ New screens (add to UI class)
- ✅ Power-ups (extend Tetromino class)

### Requires More Work
- 🔶 Multiplayer (needs networking layer)
- 🔶 3D graphics (needs different rendering)
- 🔶 Online leaderboard (needs backend)

## Code Quality Metrics

### Maintainability
- **Lines of Code**: ~1500 total
- **Cyclomatic Complexity**: Low (simple functions)
- **Coupling**: Loose (modules independent)
- **Cohesion**: High (related code together)

### Documentation
- ✅ Module docstrings
- ✅ Class docstrings
- ✅ Function docstrings
- ✅ Inline comments
- ✅ Type hints (where applicable)

## Testing Strategy (Future)

### Unit Tests
```python
test_tetromino.py:
- test_rotation()
- test_get_blocks()
- test_clone()

test_grid.py:
- test_collision_detection()
- test_row_clearing()
- test_lock_piece()

test_game.py:
- test_scoring()
- test_level_progression()
- test_game_over()
```

### Integration Tests
- Test game loop cycles
- Test state transitions
- Test full gameplay scenarios

## Lessons Learned

### What Works Well
1. **Modular design**: Easy to find and fix bugs
2. **Configuration class**: Simple to tweak game balance
3. **OOP structure**: Clear responsibilities
4. **Documentation**: Easy for others to understand

### What Could Be Improved
1. **Event system**: Could use observer pattern
2. **Save/Load**: Add game state persistence
3. **Settings menu**: Make config user-adjustable
4. **Animation**: Add smooth piece movement

## Best Practices Demonstrated

### Python
- PEP 8 style guide
- Descriptive variable names
- List comprehensions
- Type hints where helpful

### Game Development
- Fixed time step
- Input buffering
- State machine
- Component separation

### Software Engineering
- DRY principle (Don't Repeat Yourself)
- SOLID principles (where applicable)
- Clear documentation
- Version control ready

## Further Reading
- [Game Programming Patterns](https://gameprogrammingpatterns.com/)
- [Python Design Patterns](https://refactoring.guru/design-patterns/python)
- [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
