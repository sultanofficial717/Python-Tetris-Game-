# Contributing to Python Tetris Game

First off, thank you for considering contributing to Python Tetris Game! 🎉

This is an educational project, and contributions that help others learn are especially welcome.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

### Our Pledge
- Be respectful and inclusive
- Welcome newcomers and beginners
- Provide constructive feedback
- Focus on education and learning

### Unacceptable Behavior
- Harassment or discriminatory language
- Trolling or insulting comments
- Posting others' private information
- Unethical or illegal conduct

## 💡 How Can I Contribute?

### Reporting Bugs 🐛
1. Check if the bug was already reported in [Issues](https://github.com/sultanofficial717/Python-Tetris-Game-/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment (OS, Python version)

### Suggesting Enhancements ✨
1. Check existing [Issues](https://github.com/sultanofficial717/Python-Tetris-Game-/issues) and [Pull Requests](https://github.com/sultanofficial717/Python-Tetris-Game-/pulls)
2. Create an issue describing:
   - The enhancement
   - Why it would be useful
   - How it could be implemented
   - Educational value it adds

### Code Contributions 💻

#### Great First Contributions
- Fix typos in documentation
- Improve code comments
- Add more examples
- Enhance error messages
- Write unit tests
- Improve README

#### Feature Ideas
- 🔊 Sound effects and music
- 🎨 Custom themes and skins
- 💾 Save/load game state
- 🏆 Online leaderboards
- 🎮 Gamepad support
- 📱 Mobile controls
- 🌐 Internationalization (i18n)
- 🎯 Achievement system
- 📊 Statistics tracking
- 🎬 Replay system

## 🛠️ Development Setup

### 1. Fork and Clone
```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR-USERNAME/Python-Tetris-Game-.git
cd Python-Tetris-Game-
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install -e .  # Install project in editable mode
```

### 4. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 5. Make Changes
- Write clean, documented code
- Follow style guidelines (see below)
- Test your changes thoroughly

### 6. Run Tests (when available)
```bash
pytest tests/
```

## 📝 Style Guidelines

### Python Code Style

#### Follow PEP 8
```python
# Good
def calculate_score(lines_cleared, level):
    """Calculate score based on lines and level."""
    base_score = lines_cleared * 100
    return base_score * level

# Bad
def calc_scr(l,lv):
    bs=l*100
    return bs*lv
```

#### Naming Conventions
- **Classes**: `PascalCase` (e.g., `TetrisGame`, `Tetromino`)
- **Functions/Variables**: `snake_case` (e.g., `calculate_score`, `game_state`)
- **Constants**: `UPPER_CASE` (e.g., `SCREEN_WIDTH`, `MAX_LEVEL`)
- **Private members**: `_leading_underscore` (e.g., `_internal_state`)

#### Documentation
```python
def clear_full_rows(self):
    """
    Clear all full rows and move rows above down.
    
    Returns:
        int: Number of rows cleared
        
    Algorithm:
    1. Find all full rows
    2. Remove full rows
    3. Add empty rows at top
    
    Educational Note:
    This demonstrates list manipulation and game grid management.
    """
    # Implementation...
```

### Documentation Style

#### Be Educational
Since this is an educational project, explain WHY, not just WHAT:

```python
# Good
# We use a 2D list to represent the grid where 0 = empty
# and color tuples = filled cells. This allows O(1) lookup
# and makes collision detection straightforward.
self.grid = [[0] * cols for _ in range(rows)]

# Bad
# Initialize grid
self.grid = [[0] * cols for _ in range(rows)]
```

#### Include Examples
```python
def rotate_clockwise(self):
    """
    Rotate 90° clockwise.
    
    Example:
        Before:        After:
        [1, 0]        [1, 1]
        [1, 1]  -->   [0, 1]
    """
```

### Commit Message Style

#### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

#### Examples
```
feat(game): add pause functionality

- Added pause state to game
- Press P to pause/unpause
- Display pause overlay

Closes #42
```

```
fix(collision): resolve wall-kick rotation issue

- Fixed bug where pieces could rotate through walls
- Added additional boundary checks
- Updated unit tests

Fixes #38
```

```
docs(readme): improve installation instructions

- Added virtual environment steps
- Clarified Python version requirements
- Added troubleshooting section
```

## 🔄 Pull Request Process

### Before Submitting
1. ✅ Code follows style guidelines
2. ✅ Documentation is updated
3. ✅ Code is tested
4. ✅ Commit messages are clear
5. ✅ Branch is up to date with main

### PR Checklist
```markdown
## Description
[Clear description of changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Testing
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Tested on Linux
- [ ] Added/updated tests

## Documentation
- [ ] Updated README if needed
- [ ] Updated code comments
- [ ] Updated docs/ if needed

## Educational Value
[How does this help learners?]
```

### Review Process
1. Maintainer reviews code
2. Feedback provided (if needed)
3. You make requested changes
4. Once approved, PR is merged

### After Merging
- Delete your branch
- Pull latest main
- Update your fork

## 🎓 Educational Standards

Since this is an educational project, please ensure:

### Code Quality
- Clear variable names
- Well-documented functions
- Logical organization
- No "magic numbers"

### Documentation
- Explain complex algorithms
- Provide examples
- Link to resources
- Teach concepts, not just syntax

### Simplicity
- Favor readability over cleverness
- Break complex logic into smaller functions
- Use clear control flow
- Avoid premature optimization

## 📚 Resources

### Learning Python
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Real Python](https://realpython.com/)

### Learning Pygame
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Pygame Tutorial](https://www.pygame.org/wiki/tutorials)

### Game Development
- [Game Programming Patterns](https://gameprogrammingpatterns.com/)
- [Gamasutra](https://www.gamasutra.com/)

### Git & GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Docs](https://docs.github.com/)

## 🎯 Contribution Ideas by Skill Level

### Beginner
- Fix typos
- Improve comments
- Add docstrings
- Update README

### Intermediate
- Add unit tests
- Implement sound effects
- Create new themes
- Add game statistics

### Advanced
- Multiplayer support
- AI opponent
- Level editor
- Online features

## 💬 Getting Help

- **Questions**: Open a [Discussion](https://github.com/sultanofficial717/Python-Tetris-Game-/discussions)
- **Bugs**: Create an [Issue](https://github.com/sultanofficial717/Python-Tetris-Game-/issues)
- **Ideas**: Start a [Discussion](https://github.com/sultanofficial717/Python-Tetris-Game-/discussions)

## 🙏 Thank You!

Your contributions help make this project a better learning resource for everyone!

---

**Happy Contributing! 🚀**
