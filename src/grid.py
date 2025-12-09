"""
Grid Module
===========

This module manages the game grid where tetrominoes are placed and cleared.
It handles collision detection, row clearing, and grid state management.

Educational Purpose:
-------------------
Learn about:
- 2D array manipulation
- Collision detection algorithms
- Grid-based game mechanics
- List comprehensions in Python
"""

from .config import Config


class Grid:
    """
    Manages the Tetris game grid/board.
    
    The grid is a 2D list where:
    - 0 represents an empty cell
    - A color tuple represents a filled cell
    
    Attributes:
        grid (list): 2D list representing the game board
        rows (int): Number of rows in the grid
        cols (int): Number of columns in the grid
    """
    
    def __init__(self):
        """Initialize an empty grid."""
        self.rows = Config.ROWS
        self.cols = Config.COLUMNS
        self.grid = [[0] * self.cols for _ in range(self.rows)]
    
    def is_valid_position(self, tetromino, offset_x=0, offset_y=0):
        """
        Check if a tetromino can be placed at a given position.
        
        Args:
            tetromino (Tetromino): The tetromino to check
            offset_x (int): Horizontal offset from current position
            offset_y (int): Vertical offset from current position
            
        Returns:
            bool: True if position is valid, False otherwise
            
        A position is invalid if:
        - Any block is outside grid bounds
        - Any block overlaps with a filled cell
        """
        for row_idx, row in enumerate(tetromino.shape):
            for col_idx, cell in enumerate(row):
                if cell:  # If this cell is filled
                    new_x = tetromino.x + col_idx + offset_x
                    new_y = tetromino.y + row_idx + offset_y
                    
                    # Check horizontal bounds
                    if new_x < 0 or new_x >= self.cols:
                        return False
                    
                    # Check bottom bound
                    if new_y >= self.rows:
                        return False
                    
                    # Check collision with placed blocks (ignore if above grid)
                    if new_y >= 0 and self.grid[new_y][new_x]:
                        return False
        
        return True
    
    def lock_tetromino(self, tetromino):
        """
        Lock a tetromino into the grid permanently.
        
        Args:
            tetromino (Tetromino): The tetromino to lock in place
            
        This is called when a tetromino can no longer fall.
        """
        for row_idx, row in enumerate(tetromino.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    grid_x = tetromino.x + col_idx
                    grid_y = tetromino.y + row_idx
                    if 0 <= grid_y < self.rows:
                        self.grid[grid_y][grid_x] = tetromino.color
    
    def clear_full_rows(self):
        """
        Clear all full rows and move rows above down.
        
        Returns:
            int: Number of rows cleared
            
        Algorithm:
        1. Find all full rows (all cells filled)
        2. Remove full rows
        3. Add empty rows at the top
        """
        rows_cleared = 0
        row_idx = self.rows - 1
        
        while row_idx >= 0:
            if all(self.grid[row_idx]):  # Row is full
                del self.grid[row_idx]
                self.grid.insert(0, [0] * self.cols)  # Add empty row at top
                rows_cleared += 1
                # Don't decrement row_idx, check same position again
            else:
                row_idx -= 1
        
        return rows_cleared
    
    def is_game_over(self):
        """
        Check if the game is over.
        
        Returns:
            bool: True if top row has any filled cells
            
        Game over occurs when blocks stack to the top of the grid.
        """
        return any(self.grid[0])
    
    def get_filled_cells(self):
        """
        Get all filled cell positions and their colors.
        
        Returns:
            list: List of ((x, y), color) tuples
            
        Useful for rendering the grid.
        """
        filled = []
        for y in range(self.rows):
            for x in range(self.cols):
                if self.grid[y][x]:
                    filled.append(((x, y), self.grid[y][x]))
        return filled
    
    def clear(self):
        """Reset the grid to empty state."""
        self.grid = [[0] * self.cols for _ in range(self.rows)]
    
    def get_height(self):
        """
        Get the current height of stacked blocks.
        
        Returns:
            int: Number of rows from bottom containing blocks
        """
        for y in range(self.rows):
            if any(self.grid[y]):
                return self.rows - y
        return 0
    
    def __str__(self):
        """
        String representation for debugging.
        
        Returns:
            str: ASCII representation of the grid
        """
        result = []
        for row in self.grid:
            row_str = ''.join(['█' if cell else '·' for cell in row])
            result.append(row_str)
        return '\n'.join(result)
