# Game Mechanics Documentation

## Overview
This document provides a detailed explanation of the Tetris game mechanics implementation.

## Core Game Concepts

### Tetrominoes
Tetrominoes are geometric shapes composed of four square blocks each. The game features seven distinct shapes:

1. **I-Block (Line)**
   ```
   ████
   ```
   - Most valuable for creating Tetrises
   - 4 blocks in a row

2. **O-Block (Square)**
   ```
   ██
   ██
   ```
   - Doesn't rotate
   - Stable piece

3. **T-Block**
   ```
    █
   ███
   ```
   - Versatile shape
   - Can fit many situations

4. **L-Block**
   ```
   █
   █
   ███
   ```
   - Corner piece
   - Good for building structures

5. **J-Block**
   ```
     █
     █
   ███
   ```
   - Mirror of L-block

6. **S-Block**
   ```
    ██
   ██
   ```
   - Zigzag shape

7. **Z-Block**
   ```
   ██
    ██
   ```
   - Opposite of S-block

## Game Mechanics

### Piece Movement
- **Horizontal Movement**: Pieces can move left or right one cell at a time
- **Vertical Movement**: Pieces fall automatically based on game speed
- **Rotation**: Pieces rotate 90 degrees clockwise with wall-kick support

### Wall Kick System
When a piece rotates near walls or other pieces:
1. First, try rotation at current position
2. If collision detected, try offsetting by 1 cell left
3. Try offsetting by 1 cell right
4. Try offsetting by 2 cells left
5. Try offsetting by 2 cells right
6. If all fail, rotation is cancelled

### Collision Detection
The game checks for collisions in three scenarios:
1. **Horizontal boundaries**: Piece cannot move outside grid
2. **Vertical boundaries**: Piece cannot fall below grid
3. **Other pieces**: Piece cannot overlap with locked pieces

### Line Clearing
When a horizontal line is completely filled:
1. The line is removed
2. All lines above shift down one row
3. An empty line is added at the top
4. Score is calculated based on lines cleared

### Scoring System

#### Base Points
| Lines Cleared | Points | Multiplier |
|--------------|--------|------------|
| 1 line       | 100    | 1x         |
| 2 lines      | 250    | 2.5x       |
| 3 lines      | 500    | 5x         |
| 4 lines      | 1000   | 10x        |

#### Bonus Points
- **Soft Drop**: +1 point per cell dropped
- **Hard Drop**: +2 points per cell dropped

Formula: `score = base_points × lines_cleared × multiplier + drop_bonus`

### Level Progression
- Player starts at Level 1
- Every 10 lines cleared advances to next level
- Each level increases fall speed
- Maximum level: 20 (or unlimited in some implementations)

### Speed Calculation
```
fall_speed = max(100ms, 500ms - (level × 50ms))
```

- Level 1: 500ms per cell
- Level 5: 250ms per cell
- Level 9+: 100ms per cell (maximum speed)

## Advanced Mechanics

### Ghost Piece
- A translucent preview showing where the piece will land
- Updates in real-time as piece moves
- Helps players plan placement

### Next Piece Preview
- Shows the next piece to spawn
- Allows strategic planning
- Essential for advanced play

### Game Over Condition
Game ends when:
- A new piece spawns
- The spawn position is already occupied
- Indicates grid is full

## Strategic Elements

### T-Spins (Future Enhancement)
- Special rotation maneuvers with T-pieces
- Awards bonus points
- Requires advanced collision detection

### Combos (Future Enhancement)
- Clearing lines on consecutive drops
- Multiplies score
- Encourages aggressive play

### Hold Feature (Future Enhancement)
- Ability to save current piece for later
- Can only hold one piece at a time
- Swaps with held piece when activated

## Physics and Timing

### Frame Rate
- Game runs at 60 FPS
- Ensures smooth animation
- Consistent input responsiveness

### Auto-Repeat
- Holding direction key moves piece repeatedly
- Initial delay: 250ms
- Repeat rate: 50ms

### Lock Delay
- Time before piece locks after touching ground
- Default: 500ms
- Allows last-moment adjustments

## Educational Notes

### Why These Mechanics?
1. **Simplicity**: Core rules are easy to understand
2. **Depth**: Mastery requires skill and strategy
3. **Fairness**: RNG is controlled by 7-bag system (future)
4. **Progression**: Gradual difficulty increase
5. **Reward**: Multiple scoring strategies

### Learning Outcomes
- Understanding game balance
- Implementing physics-based movement
- Creating responsive controls
- Designing progression systems
- Balancing difficulty curves

## Implementation Details

### Grid System
- 10 columns × 20 rows (standard)
- Each cell: 30×30 pixels
- Grid stored as 2D array

### Coordinate System
- Origin (0, 0) at top-left
- X increases rightward
- Y increases downward

### State Management
Game cycles through states:
1. Menu
2. Login
3. Playing
4. Paused
5. Game Over

Each state has dedicated logic and rendering.

## References
- [Tetris Guideline](https://tetris.wiki/Tetris_Guideline)
- [Super Rotation System](https://tetris.wiki/Super_Rotation_System)
- [Tetris Wiki](https://tetris.wiki/)
