# renderer.py
import pygame
# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
GOLD = (255, 215, 0)

# Game Settings
GRID_SIZE = 7  # 7x7 Board Grid
TIGER_COUNT = 1
GOAT_COUNT = 15

class Renderer:
    def __init__(self, game_logic):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Shein Bakri Game")
        self.game_logic = game_logic
        self.cell_size = SCREEN_WIDTH // self.game_logic.grid_size

    def draw_board(self):
        self.screen.fill(WHITE)
        for i in range(self.game_logic.grid_size):
            pygame.draw.line(self.screen, BLACK, (i * self.cell_size, 0), (i * self.cell_size, SCREEN_HEIGHT), 2)
            pygame.draw.line(self.screen, BLACK, (0, i * self.cell_size), (SCREEN_WIDTH, i * self.cell_size), 2)
        pygame.draw.rect(self.screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 3)
    
    def draw_pieces(self):
        # Draw the tiger
        tiger_x, tiger_y = self.game_logic.tiger_position
        pygame.draw.circle(self.screen, GOLD, ((tiger_x * self.cell_size) + self.cell_size // 2, (tiger_y * self.cell_size) + self.cell_size // 2), self.cell_size // 3)
        
        # Draw the goats
        for goat_x, goat_y in self.game_logic.goat_positions:
            pygame.draw.circle(self.screen, BROWN, ((goat_x * self.cell_size) + self.cell_size // 2, (goat_y * self.cell_size) + self.cell_size // 2), self.cell_size // 4)
    
    def render(self):
        self.draw_board()
        self.draw_pieces()
        pygame.display.flip()
