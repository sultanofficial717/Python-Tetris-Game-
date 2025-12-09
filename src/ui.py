"""
UI Module - User Interface Components
======================================

This module handles all user interface rendering including:
- Welcome screen
- Login screen
- Game header
- Sidebar with game info
- Pause menu
- Game over screen

Educational Purpose:
-------------------
Learn about:
- UI/UX design in games
- Pygame drawing functions
- Event handling
- Screen layout and composition
"""

import pygame
import sys
from .config import Config


class UI:
    """
    Manages all user interface elements and screens.
    
    Attributes:
        screen (pygame.Surface): The game display surface
        clock (pygame.time.Clock): Game clock for timing
    """
    
    def __init__(self, screen, clock):
        """
        Initialize UI manager.
        
        Args:
            screen (pygame.Surface): Pygame display surface
            clock (pygame.time.Clock): Game clock
        """
        self.screen = screen
        self.clock = clock
    
    def draw_welcome_screen(self):
        """
        Display the welcome/title screen.
        
        Returns:
            bool: True to start game, False to quit
        """
        running = True
        
        while running:
            self.screen.fill(Config.GAME_BG)
            
            # Title
            title = Config.FONT_HUGE.render("TETRIS", True, Config.CYAN)
            title_rect = title.get_rect(center=(Config.SCREEN_WIDTH // 2, 150))
            self.screen.blit(title, title_rect)
            
            # Subtitle
            subtitle = Config.FONT_MEDIUM.render(
                "Classic Puzzle Game", True, Config.WHITE
            )
            subtitle_rect = subtitle.get_rect(
                center=(Config.SCREEN_WIDTH // 2, 220)
            )
            self.screen.blit(subtitle, subtitle_rect)
            
            # Instructions
            instructions = [
                "Press ENTER to Start",
                "Press ESC to Quit",
                "",
                "A Python Game Development Project"
            ]
            
            y_offset = 300
            for text in instructions:
                if text:
                    rendered = Config.FONT_SMALL.render(text, True, Config.LIGHT_GRAY)
                else:
                    y_offset += 10
                    continue
                text_rect = rendered.get_rect(
                    center=(Config.SCREEN_WIDTH // 2, y_offset)
                )
                self.screen.blit(rendered, text_rect)
                y_offset += 35
            
            # Footer
            footer = Config.FONT_SMALL.render(
                "© 2025 - Educational Purpose", True, Config.GRAY
            )
            footer_rect = footer.get_rect(
                center=(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT - 30)
            )
            self.screen.blit(footer, footer_rect)
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
                    if event.key == pygame.K_ESCAPE:
                        return False
            
            pygame.display.flip()
            self.clock.tick(Config.FPS)
        
        return False
    
    def draw_login_screen(self):
        """
        Display login screen to get player name.
        
        Returns:
            str: Player name (or "Player" if cancelled)
        """
        input_box = pygame.Rect(
            Config.SCREEN_WIDTH // 2 - 150,
            Config.SCREEN_HEIGHT // 2 - 20,
            300, 50
        )
        color_inactive = Config.GRAY
        color_active = Config.CYAN
        color = color_inactive
        active = False
        text = ""
        
        running = True
        while running:
            self.screen.fill(Config.GAME_BG)
            
            # Title
            title = Config.FONT_LARGE.render(
                "Enter Your Name", True, Config.WHITE
            )
            title_rect = title.get_rect(
                center=(Config.SCREEN_WIDTH // 2, 150)
            )
            self.screen.blit(title, title_rect)
            
            # Instruction
            instruction = Config.FONT_SMALL.render(
                "Press ENTER to continue or ESC to skip", 
                True, Config.LIGHT_GRAY
            )
            instr_rect = instruction.get_rect(
                center=(Config.SCREEN_WIDTH // 2, 220)
            )
            self.screen.blit(instruction, instr_rect)
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    active = input_box.collidepoint(event.pos)
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return text if text else "Player"
                    elif event.key == pygame.K_ESCAPE:
                        return "Player"
                    elif active:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif len(text) < 15:  # Max length
                            text += event.unicode
            
            # Draw input box
            txt_surface = Config.FONT_MEDIUM.render(text, True, Config.WHITE)
            width = max(300, txt_surface.get_width() + 20)
            input_box.w = width
            input_box.centerx = Config.SCREEN_WIDTH // 2
            
            pygame.draw.rect(self.screen, color, input_box, 3)
            self.screen.blit(
                txt_surface, 
                (input_box.x + 10, input_box.y + 10)
            )
            
            pygame.display.flip()
            self.clock.tick(Config.FPS)
        
        return "Player"
    
    def draw_game_header(self, player_name, score, level, high_score):
        """
        Draw the header bar with game information.
        
        Args:
            player_name (str): Player's name
            score (int): Current score
            level (int): Current level
            high_score (int): High score
        """
        # Header background
        pygame.draw.rect(
            self.screen, Config.HEADER_BG,
            (0, 0, Config.SCREEN_WIDTH, 80)
        )
        
        # Title
        title = Config.FONT_LARGE.render("TETRIS", True, Config.WHITE)
        self.screen.blit(title, (20, 20))
        
        # Player name
        name_text = Config.FONT_SMALL.render(
            f"Player: {player_name}", True, Config.WHITE
        )
        self.screen.blit(name_text, (200, 25))
        
        # Score
        score_text = Config.FONT_SMALL.render(
            f"Score: {score}", True, Config.WHITE
        )
        self.screen.blit(score_text, (200, 50))
        
        # Level
        level_text = Config.FONT_SMALL.render(
            f"Level: {level}", True, Config.WHITE
        )
        self.screen.blit(level_text, (400, 25))
        
        # High Score
        high_text = Config.FONT_SMALL.render(
            f"High: {high_score}", True, Config.WHITE
        )
        self.screen.blit(high_text, (400, 50))
    
    def draw_sidebar(self, next_tetromino, lines_cleared, controls_visible=True):
        """
        Draw sidebar with next piece and controls.
        
        Args:
            next_tetromino (Tetromino): Next piece to display
            lines_cleared (int): Total lines cleared
            controls_visible (bool): Whether to show controls
        """
        sidebar_x = Config.GAME_WIDTH + 20
        
        # Next Piece Section
        pygame.draw.rect(
            self.screen, Config.SIDEBAR_BG,
            (sidebar_x, 100, 200, 150)
        )
        
        next_text = Config.FONT_MEDIUM.render("NEXT", True, Config.WHITE)
        self.screen.blit(next_text, (sidebar_x + 70, 110))
        
        # Draw next tetromino preview
        if next_tetromino:
            offset_x = sidebar_x + 60
            offset_y = 160
            for row_idx, row in enumerate(next_tetromino.shape):
                for col_idx, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(
                            self.screen, next_tetromino.color,
                            (offset_x + col_idx * 20, 
                             offset_y + row_idx * 20, 
                             20, 20)
                        )
                        pygame.draw.rect(
                            self.screen, Config.WHITE,
                            (offset_x + col_idx * 20, 
                             offset_y + row_idx * 20, 
                             20, 20), 1
                        )
        
        # Stats Section
        pygame.draw.rect(
            self.screen, Config.SIDEBAR_BG,
            (sidebar_x, 270, 200, 80)
        )
        
        lines_text = Config.FONT_SMALL.render(
            f"Lines: {lines_cleared}", True, Config.WHITE
        )
        self.screen.blit(lines_text, (sidebar_x + 10, 285))
        
        # Controls Section
        if controls_visible:
            pygame.draw.rect(
                self.screen, Config.SIDEBAR_BG,
                (sidebar_x, 370, 200, 200)
            )
            
            controls_title = Config.FONT_SMALL.render(
                "CONTROLS", True, Config.CYAN
            )
            self.screen.blit(controls_title, (sidebar_x + 50, 380))
            
            y_pos = 410
            control_items = [
                ("←/→", "Move"),
                ("↓", "Soft Drop"),
                ("↑", "Rotate"),
                ("SPACE", "Hard Drop"),
                ("P", "Pause"),
                ("ESC", "Quit")
            ]
            
            for key, action in control_items:
                key_text = Config.FONT_SMALL.render(
                    f"{key}: {action}", True, Config.LIGHT_GRAY
                )
                self.screen.blit(key_text, (sidebar_x + 10, y_pos))
                y_pos += 25
    
    def draw_game_over_screen(self, score, high_score):
        """
        Display game over screen.
        
        Args:
            score (int): Final score
            high_score (int): High score
            
        Returns:
            str: "restart" or "quit"
        """
        overlay = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(Config.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game Over Text
        game_over_text = Config.FONT_HUGE.render(
            "GAME OVER", True, Config.RED
        )
        text_rect = game_over_text.get_rect(
            center=(Config.SCREEN_WIDTH // 2, 200)
        )
        self.screen.blit(game_over_text, text_rect)
        
        # Score
        score_text = Config.FONT_LARGE.render(
            f"Score: {score}", True, Config.WHITE
        )
        score_rect = score_text.get_rect(
            center=(Config.SCREEN_WIDTH // 2, 280)
        )
        self.screen.blit(score_text, score_rect)
        
        # High Score
        if score >= high_score:
            high_text = Config.FONT_MEDIUM.render(
                "NEW HIGH SCORE!", True, Config.YELLOW
            )
        else:
            high_text = Config.FONT_MEDIUM.render(
                f"High Score: {high_score}", True, Config.LIGHT_GRAY
            )
        high_rect = high_text.get_rect(
            center=(Config.SCREEN_WIDTH // 2, 340)
        )
        self.screen.blit(high_text, high_rect)
        
        # Options
        restart_text = Config.FONT_SMALL.render(
            "Press ENTER to Restart", True, Config.GREEN
        )
        restart_rect = restart_text.get_rect(
            center=(Config.SCREEN_WIDTH // 2, 420)
        )
        self.screen.blit(restart_text, restart_rect)
        
        quit_text = Config.FONT_SMALL.render(
            "Press ESC to Quit", True, Config.LIGHT_GRAY
        )
        quit_rect = quit_text.get_rect(
            center=(Config.SCREEN_WIDTH // 2, 460)
        )
        self.screen.blit(quit_text, quit_rect)
        
        pygame.display.flip()
        
        # Wait for input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "restart"
                    if event.key == pygame.K_ESCAPE:
                        return "quit"
            self.clock.tick(Config.FPS)
        
        return "quit"
    
    def draw_pause_screen(self):
        """Draw pause overlay."""
        overlay = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(Config.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = Config.FONT_HUGE.render("PAUSED", True, Config.YELLOW)
        text_rect = pause_text.get_rect(
            center=(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 2)
        )
        self.screen.blit(pause_text, text_rect)
        
        continue_text = Config.FONT_SMALL.render(
            "Press P to Continue", True, Config.WHITE
        )
        continue_rect = continue_text.get_rect(
            center=(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 2 + 60)
        )
        self.screen.blit(continue_text, continue_rect)
        
        pygame.display.flip()
