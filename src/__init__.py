"""
Python Tetris Game - A Professional Educational Implementation
===============================================================

A complete, well-structured Tetris game built with Python and Pygame.
Perfect for learning game development, Python programming, and software architecture.

Author: Sultan Official
Repository: https://github.com/sultanofficial717/Python-Tetris-Game-
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Sultan Official"
__email__ = "sultanofficial717@github.com"

# Import main components when package is imported
# Allows: from src import TetrisGame
try:
    from .config import Config
    from .game import TetrisGame
    from .tetromino import Tetromino
    from .grid import Grid
    
    __all__ = ['Config', 'TetrisGame', 'Tetromino', 'Grid']
except ImportError:
    # Allow package to be imported even if dependencies aren't installed
    __all__ = []
