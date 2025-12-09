"""
Configuration Module for Tetris Game
====================================

This module contains all game configuration constants including:
- Screen dimensions and game grid settings
- Color definitions for tetrominoes and UI elements
- Tetromino shape definitions
- Game mechanics settings (speed, scoring, etc.)

Educational Purpose:
-------------------
Learn about:
- Centralized configuration management
- Constants and their importance in game development
- Color theory in game design
- Data structures for game shapes
"""

import pygame

# Initialize pygame font module
pygame.font.init()

class Config:
    """
    Central configuration class for the Tetris game.
    
    This class uses class variables to store all game settings,
    making it easy to modify game behavior from a single location.
    """
    
    # Screen and Grid Configuration
    SCREEN_WIDTH = 800  # Increased for better visibility and side panel
    SCREEN_HEIGHT = 600
    BLOCK_SIZE = 30
    
    # Calculate game grid dimensions
    GAME_WIDTH = 300
    COLUMNS = GAME_WIDTH // BLOCK_SIZE  # 10 columns
    ROWS = (SCREEN_HEIGHT - 100) // BLOCK_SIZE  # Account for header
    
    # Frame rate for smooth gameplay
    FPS = 60
    
    # Color Palette - RGB values
    # Primary Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    DARK_GRAY = (50, 50, 50)
    LIGHT_GRAY = (200, 200, 200)
    
    # Tetromino Colors (Vibrant and distinct)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    
    # UI Colors
    HEADER_BG = (34, 139, 34)  # Forest Green
    GAME_BG = (20, 20, 40)  # Dark Blue-Gray
    SIDEBAR_BG = (30, 30, 50)
    GRID_LINE = (70, 70, 90)
    
    # Tetromino color list
    COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE]
    
    # Font Configurations
    FONT_SMALL = pygame.font.Font(None, 24)
    FONT_MEDIUM = pygame.font.Font(None, 36)
    FONT_LARGE = pygame.font.Font(None, 48)
    FONT_HUGE = pygame.font.Font(None, 72)
    
    # Tetromino Shapes
    # Each shape is represented as a 2D list where 1 = filled block, 0 = empty
    SHAPES = [
        [[1, 1, 1, 1]],  # I-shape (Line)
        [[1, 1], [1, 1]],  # O-shape (Square)
        [[1, 1, 1], [0, 1, 0]],  # T-shape
        [[1, 1, 0], [0, 1, 1]],  # Z-shape
        [[0, 1, 1], [1, 1, 0]],  # S-shape
        [[1, 0, 0], [1, 1, 1]],  # L-shape
        [[0, 0, 1], [1, 1, 1]],  # J-shape
    ]
    
    # Shape names for educational display
    SHAPE_NAMES = {
        0: "I-Block",
        1: "O-Block", 
        2: "T-Block",
        3: "Z-Block",
        4: "S-Block",
        5: "L-Block",
        6: "J-Block"
    }
    
    # Game Mechanics Settings
    INITIAL_FALL_SPEED = 500  # milliseconds
    MIN_FALL_SPEED = 100  # fastest speed
    SPEED_INCREMENT = 50  # speed increase per level
    POINTS_PER_LEVEL = 100  # points needed to level up
    
    # Scoring System
    POINTS_PER_ROW = 100
    COMBO_MULTIPLIER = {
        1: 1,    # Single line
        2: 2.5,  # Double
        3: 5,    # Triple
        4: 10    # Tetris!
    }
    
    # Game States
    STATE_MENU = "menu"
    STATE_LOGIN = "login"
    STATE_PLAYING = "playing"
    STATE_PAUSED = "paused"
    STATE_GAME_OVER = "game_over"
    
    # Controls Information
    CONTROLS = {
        "Move Left": "← Arrow",
        "Move Right": "→ Arrow",
        "Soft Drop": "↓ Arrow",
        "Hard Drop": "Space",
        "Rotate": "↑ Arrow",
        "Pause": "P",
        "Quit": "ESC"
    }
    
    @classmethod
    def get_level_speed(cls, level):
        """
        Calculate fall speed based on current level.
        
        Args:
            level (int): Current game level
            
        Returns:
            int: Fall speed in milliseconds
        """
        speed = cls.INITIAL_FALL_SPEED - (level * cls.SPEED_INCREMENT)
        return max(cls.MIN_FALL_SPEED, speed)
    
    @classmethod
    def calculate_score(cls, rows_cleared):
        """
        Calculate score based on number of rows cleared at once.
        
        Args:
            rows_cleared (int): Number of rows cleared simultaneously
            
        Returns:
            int: Points earned
        """
        if rows_cleared == 0:
            return 0
        multiplier = cls.COMBO_MULTIPLIER.get(rows_cleared, 1)
        return int(cls.POINTS_PER_ROW * rows_cleared * multiplier)
