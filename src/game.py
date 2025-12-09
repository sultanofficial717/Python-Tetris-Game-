"""
Game Module - Main Game Logic
==============================

This module contains the TetrisGame class that orchestrates all game components:
- Game loop management
- Input handling
- Collision detection
- Scoring system
- Game state management

Educational Purpose:
-------------------
Learn about:
- Game loop architecture
- State machine pattern
- Event-driven programming
- Game physics and timing
"""

import pygame
import sys
from .config import Config
from .tetromino import Tetromino
from .grid import Grid
from .ui import UI


class TetrisGame:
    """
    Main game class that manages the Tetris game flow.
    
    This class implements the game loop pattern and coordinates
    all game components (grid, pieces, UI, input).
    
    Attributes:
        screen (pygame.Surface): Game display surface
        clock (pygame.time.Clock): Game clock for FPS control
        grid (Grid): Game grid/board
        ui (UI): User interface manager
        current_piece (Tetromino): Currently falling piece
        next_piece (Tetromino): Next piece to spawn
        state (str): Current game state
        score (int): Current score
        level (int): Current level
        lines_cleared (int): Total lines cleared
        high_score (int): Highest score achieved
        player_name (str): Player's name
    """
    
    def __init__(self):
        """Initialize the game."""
        # Initialize Pygame
        pygame.init()
        
        # Setup display
        self.screen = pygame.display.set_mode(
            (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Tetris - Python Game Development Project")
        
        # Game clock
        self.clock = pygame.time.Clock()
        
        # Initialize components
        self.grid = Grid()
        self.ui = UI(self.screen, self.clock)
        
        # Game state
        self.state = Config.STATE_MENU
        self.reset_game()
        
        # High score (persists across games)
        self.high_score = 0
    
    def reset_game(self):
        """Reset game state for a new game."""
        self.grid.clear()
        self.current_piece = Tetromino()
        self.next_piece = Tetromino()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_time = 0
        self.fall_speed = Config.get_level_speed(self.level)
        self.paused = False
        self.player_name = "Player"
    
    def handle_input(self):
        """
        Handle user input events.
        
        This method processes keyboard input for:
        - Piece movement (left, right, down)
        - Piece rotation
        - Hard drop
        - Pause
        - Quit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            
            if event.type == pygame.KEYDOWN:
                # Pause toggle
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                    if self.paused:
                        self.ui.draw_pause_screen()
                    return
                
                # Quit
                if event.key == pygame.K_ESCAPE:
                    self.state = Config.STATE_GAME_OVER
                    return
                
                # Skip if paused
                if self.paused:
                    return
                
                # Move left
                if event.key == pygame.K_LEFT:
                    if self.grid.is_valid_position(self.current_piece, -1, 0):
                        self.current_piece.x -= 1
                
                # Move right
                if event.key == pygame.K_RIGHT:
                    if self.grid.is_valid_position(self.current_piece, 1, 0):
                        self.current_piece.x += 1
                
                # Soft drop (move down faster)
                if event.key == pygame.K_DOWN:
                    if self.grid.is_valid_position(self.current_piece, 0, 1):
                        self.current_piece.y += 1
                        self.score += 1  # Bonus point for soft drop
                
                # Rotate
                if event.key == pygame.K_UP:
                    original_shape = [row[:] for row in self.current_piece.shape]
                    self.current_piece.rotate_clockwise()
                    
                    # Wall kick: try to adjust position if rotation causes collision
                    if not self.grid.is_valid_position(self.current_piece, 0, 0):
                        # Try moving left or right
                        for offset in [1, -1, 2, -2]:
                            if self.grid.is_valid_position(
                                self.current_piece, offset, 0
                            ):
                                self.current_piece.x += offset
                                break
                        else:
                            # Can't rotate, revert
                            self.current_piece.shape = original_shape
                
                # Hard drop (instant drop to bottom)
                if event.key == pygame.K_SPACE:
                    drop_distance = 0
                    while self.grid.is_valid_position(self.current_piece, 0, 1):
                        self.current_piece.y += 1
                        drop_distance += 1
                    self.score += drop_distance * 2  # Bonus points
                    self.lock_current_piece()
    
    def lock_current_piece(self):
        """
        Lock the current piece into the grid and spawn next piece.
        
        This method:
        1. Places current piece on grid
        2. Clears full rows
        3. Updates score
        4. Spawns next piece
        5. Checks for game over
        """
        # Lock piece into grid
        self.grid.lock_tetromino(self.current_piece)
        
        # Clear full rows and update score
        rows = self.grid.clear_full_rows()
        if rows > 0:
            self.lines_cleared += rows
            points = Config.calculate_score(rows)
            self.score += points
            
            # Level up every 10 lines
            new_level = (self.lines_cleared // 10) + 1
            if new_level > self.level:
                self.level = new_level
                self.fall_speed = Config.get_level_speed(self.level)
        
        # Spawn next piece
        self.current_piece = self.next_piece
        self.next_piece = Tetromino()
        
        # Check game over
        if not self.grid.is_valid_position(self.current_piece, 0, 0):
            self.state = Config.STATE_GAME_OVER
            if self.score > self.high_score:
                self.high_score = self.score
    
    def update(self):
        """
        Update game state.
        
        This method handles automatic piece falling based on the game timer.
        """
        if self.paused:
            return
        
        # Update fall timer
        self.fall_time += self.clock.get_rawtime()
        
        # Check if piece should fall
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            
            # Try to move piece down
            if self.grid.is_valid_position(self.current_piece, 0, 1):
                self.current_piece.y += 1
            else:
                # Piece has landed
                self.lock_current_piece()
    
    def draw_grid(self):
        """Draw the game grid and all placed blocks."""
        # Draw grid background
        pygame.draw.rect(
            self.screen, Config.GAME_BG,
            (0, 80, Config.GAME_WIDTH, Config.SCREEN_HEIGHT - 80)
        )
        
        # Draw grid lines
        for x in range(Config.COLUMNS + 1):
            pygame.draw.line(
                self.screen, Config.GRID_LINE,
                (x * Config.BLOCK_SIZE, 80),
                (x * Config.BLOCK_SIZE, Config.SCREEN_HEIGHT),
                1
            )
        
        for y in range(Config.ROWS + 1):
            pygame.draw.line(
                self.screen, Config.GRID_LINE,
                (0, y * Config.BLOCK_SIZE + 80),
                (Config.GAME_WIDTH, y * Config.BLOCK_SIZE + 80),
                1
            )
        
        # Draw placed blocks
        for (x, y), color in self.grid.get_filled_cells():
            pygame.draw.rect(
                self.screen, color,
                (x * Config.BLOCK_SIZE, y * Config.BLOCK_SIZE + 80,
                 Config.BLOCK_SIZE, Config.BLOCK_SIZE)
            )
            pygame.draw.rect(
                self.screen, Config.WHITE,
                (x * Config.BLOCK_SIZE, y * Config.BLOCK_SIZE + 80,
                 Config.BLOCK_SIZE, Config.BLOCK_SIZE),
                1
            )
    
    def draw_current_piece(self):
        """Draw the currently falling piece."""
        for row_idx, row in enumerate(self.current_piece.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = (self.current_piece.x + col_idx) * Config.BLOCK_SIZE
                    y = (self.current_piece.y + row_idx) * Config.BLOCK_SIZE + 80
                    
                    pygame.draw.rect(
                        self.screen, self.current_piece.color,
                        (x, y, Config.BLOCK_SIZE, Config.BLOCK_SIZE)
                    )
                    pygame.draw.rect(
                        self.screen, Config.WHITE,
                        (x, y, Config.BLOCK_SIZE, Config.BLOCK_SIZE),
                        1
                    )
    
    def draw_ghost_piece(self):
        """Draw a ghost/shadow of where the piece will land."""
        # Find landing position
        ghost_y = self.current_piece.y
        while self.grid.is_valid_position(self.current_piece, 0, ghost_y - self.current_piece.y + 1):
            ghost_y += 1
        
        # Draw ghost piece (semi-transparent)
        for row_idx, row in enumerate(self.current_piece.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = (self.current_piece.x + col_idx) * Config.BLOCK_SIZE
                    y = (ghost_y + row_idx) * Config.BLOCK_SIZE + 80
                    
                    # Draw as outline only
                    pygame.draw.rect(
                        self.screen, self.current_piece.color,
                        (x, y, Config.BLOCK_SIZE, Config.BLOCK_SIZE),
                        2
                    )
    
    def render(self):
        """Render all game elements."""
        self.screen.fill(Config.BLACK)
        
        # Draw header
        self.ui.draw_game_header(
            self.player_name, self.score, 
            self.level, self.high_score
        )
        
        # Draw game area
        self.draw_grid()
        self.draw_ghost_piece()
        self.draw_current_piece()
        
        # Draw sidebar
        self.ui.draw_sidebar(self.next_piece, self.lines_cleared)
        
        # Draw pause overlay if paused
        if self.paused:
            self.ui.draw_pause_screen()
        
        pygame.display.flip()
    
    def run_menu(self):
        """Run the menu state."""
        if self.ui.draw_welcome_screen():
            self.state = Config.STATE_LOGIN
        else:
            self.quit_game()
    
    def run_login(self):
        """Run the login state."""
        self.player_name = self.ui.draw_login_screen()
        self.reset_game()
        self.state = Config.STATE_PLAYING
    
    def run_playing(self):
        """Run the main game loop."""
        self.handle_input()
        self.update()
        self.render()
        self.clock.tick(Config.FPS)
    
    def run_game_over(self):
        """Run the game over state."""
        action = self.ui.draw_game_over_screen(self.score, self.high_score)
        if action == "restart":
            self.state = Config.STATE_LOGIN
        else:
            self.quit_game()
    
    def run(self):
        """
        Main game loop.
        
        This method manages different game states and runs the appropriate
        logic for each state.
        """
        running = True
        
        while running:
            if self.state == Config.STATE_MENU:
                self.run_menu()
            elif self.state == Config.STATE_LOGIN:
                self.run_login()
            elif self.state == Config.STATE_PLAYING:
                self.run_playing()
            elif self.state == Config.STATE_GAME_OVER:
                self.run_game_over()
        
        pygame.quit()
        sys.exit()
    
    def quit_game(self):
        """Quit the game cleanly."""
        pygame.quit()
        sys.exit()
