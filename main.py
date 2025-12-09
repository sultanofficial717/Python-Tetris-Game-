#!/usr/bin/env python3
"""
Python Tetris Game - Main Entry Point
======================================

A professional, educational implementation of the classic Tetris game.

This is the main launcher file that initializes and starts the game.
The actual game logic is modularized in the src/ package.

Author: Sultan Official
Repository: https://github.com/sultanofficial717/Python-Tetris-Game-
License: MIT

Educational Purpose:
-------------------
This project demonstrates:
- Clean code architecture with separation of concerns
- Object-oriented programming in Python
- Game development with Pygame
- Professional project structure
- Comprehensive documentation

How to Run:
----------
    python main.py

Or after installation:
    pip install -e .
    tetris

Requirements:
------------
- Python 3.7 or higher
- Pygame 2.0 or higher

For more information, see README.md
"""

import sys
import os

# Add src directory to Python path
# This allows importing from src package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.game import TetrisGame
except ImportError as e:
    print("Error: Could not import game modules.")
    print(f"Details: {e}")
    print("\nPlease ensure:")
    print("1. All files in src/ directory are present")
    print("2. Pygame is installed: pip install pygame")
    print("3. You're running from the project root directory")
    sys.exit(1)


def main():
    """
    Main entry point for the Tetris game.
    
    This function:
    1. Creates a TetrisGame instance
    2. Starts the game loop
    3. Handles clean exit
    
    The game will run until the player quits.
    """
    try:
        # Create game instance
        game = TetrisGame()
        
        # Run the game
        # This enters the main game loop
        game.run()
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nGame interrupted by user.")
        print("Thanks for playing!")
        sys.exit(0)
        
    except Exception as e:
        # Catch any unexpected errors
        print(f"\n\nAn error occurred: {e}")
        print("\nPlease report this issue at:")
        print("https://github.com/sultanofficial717/Python-Tetris-Game-/issues")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    # Display welcome message
    print("=" * 60)
    print(" " * 15 + "🎮 PYTHON TETRIS GAME 🎮")
    print("=" * 60)
    print()
    print("A professional educational game development project")
    print("Author: Sultan Official")
    print("License: MIT")
    print()
    print("Starting game...")
    print("=" * 60)
    print()
    
    # Run the game
    main()
