"""
Tetromino Module
================

This module defines the Tetromino class representing falling blocks in Tetris.
Each tetromino has a shape, color, and position on the game grid.

Educational Purpose:
-------------------
Learn about:
- Object-oriented programming (OOP) in Python
- Matrix operations and transformations
- Game object representation
- Rotation algorithms
"""

import random
from .config import Config


class Tetromino:
    """
    Represents a single Tetromino (game piece) in Tetris.
    
    Attributes:
        shape (list): 2D list representing the block pattern
        color (tuple): RGB color value
        x (int): Horizontal position on grid
        y (int): Vertical position on grid
        shape_type (int): Index of shape in Config.SHAPES
    """
    
    def __init__(self, shape_type=None):
        """
        Initialize a new Tetromino.
        
        Args:
            shape_type (int, optional): Specific shape index. 
                                       Random if None.
        """
        if shape_type is None:
            self.shape_type = random.randint(0, len(Config.SHAPES) - 1)
        else:
            self.shape_type = shape_type
            
        # Deep copy the shape to avoid modifying the original
        self.shape = [row[:] for row in Config.SHAPES[self.shape_type]]
        self.color = random.choice(Config.COLORS)
        
        # Center the tetromino at the top of the grid
        self.x = Config.COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0
    
    def rotate_clockwise(self):
        """
        Rotate the tetromino 90 degrees clockwise.
        
        Algorithm: Transpose the matrix then reverse each row
        Example:
            [1, 0]    [1, 1]
            [1, 1] -> [0, 1]
        
        This is a common matrix rotation technique used in games.
        """
        # Transpose: swap rows and columns
        transposed = list(zip(*self.shape[::-1]))
        # Convert tuples back to lists
        self.shape = [list(row) for row in transposed]
    
    def rotate_counterclockwise(self):
        """
        Rotate the tetromino 90 degrees counterclockwise.
        
        Algorithm: Reverse each row then transpose
        """
        # Reverse each row first
        reversed_rows = [row[::-1] for row in self.shape]
        # Then transpose
        transposed = list(zip(*reversed_rows[::-1]))
        self.shape = [list(row) for row in transposed]
    
    def get_blocks(self):
        """
        Get the absolute positions of all blocks in the tetromino.
        
        Returns:
            list: List of (x, y) tuples representing block positions
            
        This method is useful for collision detection and drawing.
        """
        blocks = []
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:  # If cell is filled (1)
                    blocks.append((
                        self.x + col_idx,
                        self.y + row_idx
                    ))
        return blocks
    
    def get_width(self):
        """
        Get the width of the tetromino shape.
        
        Returns:
            int: Width in blocks
        """
        return len(self.shape[0]) if self.shape else 0
    
    def get_height(self):
        """
        Get the height of the tetromino shape.
        
        Returns:
            int: Height in blocks
        """
        return len(self.shape)
    
    def clone(self):
        """
        Create a copy of this tetromino.
        
        Returns:
            Tetromino: A new tetromino with the same properties
        """
        new_tetromino = Tetromino(self.shape_type)
        new_tetromino.shape = [row[:] for row in self.shape]
        new_tetromino.color = self.color
        new_tetromino.x = self.x
        new_tetromino.y = self.y
        return new_tetromino
    
    def __str__(self):
        """
        String representation for debugging.
        
        Returns:
            str: Shape name and position
        """
        shape_name = Config.SHAPE_NAMES.get(self.shape_type, "Unknown")
        return f"{shape_name} at ({self.x}, {self.y})"
