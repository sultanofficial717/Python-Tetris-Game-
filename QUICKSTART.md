# Quick Start Guide

## Run the Game Immediately

### Option 1: Simple Run
```bash
python main.py
```

### Option 2: With Virtual Environment
```bash
# Activate virtual environment (if not already active)
.venv\Scripts\activate

# Run the game
python main.py
```

## First Time Setup

If you haven't installed pygame yet:

```bash
pip install pygame
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

## Troubleshooting

### Issue: "pygame could not be resolved"
**Solution:**
```bash
pip install pygame
```

### Issue: "No module named 'src'"
**Solution:** Make sure you're running from the project root directory:
```bash
cd Python-Tetris-Game-
python main.py
```

### Issue: Game window doesn't appear
**Solution:** Check if pygame is properly installed:
```bash
python -c "import pygame; print(pygame.ver)"
```

## Controls

| Key | Action |
|-----|--------|
| **←** | Move left |
| **→** | Move right |
| **↓** | Soft drop |
| **↑** | Rotate |
| **SPACE** | Hard drop |
| **P** | Pause |
| **ESC** | Quit |

## Game Flow

1. **Welcome Screen** - Press ENTER to start
2. **Login Screen** - Enter your name (or press ESC to skip)
3. **Play Game** - Stack pieces and clear lines!
4. **Game Over** - Press ENTER to restart or ESC to quit

## Scoring

- 1 line = 100 points
- 2 lines = 250 points
- 3 lines = 500 points
- 4 lines (Tetris!) = 1000 points
- Soft drop = +1 point per cell
- Hard drop = +2 points per cell

## Tips for Beginners

1. Watch the **next piece** preview in the sidebar
2. Use the **ghost piece** (outline) to see where your piece will land
3. Try to create flat surfaces - avoid creating holes
4. Save the **I-block** for clearing 4 lines at once (Tetris!)
5. Use **hard drop** (SPACE) when you're sure of placement

## Advanced Tips

1. **T-Spin Setup** - Leave T-shaped holes for T-pieces
2. **Back-to-Back** - Clear 4 lines repeatedly for max points
3. **Flat Stacking** - Keep your stack height low and even
4. **Speed Management** - Use soft drop strategically

## Need Help?

- Read the full [README.md](README.md)
- Check [Documentation](docs/)
- View [Tutorial](docs/TUTORIAL.md)
- See [API Reference](docs/API_REFERENCE.md)

## Enjoy!

Have fun and happy gaming! 🎮

---

**Python Tetris Game** - Educational Game Development Project
