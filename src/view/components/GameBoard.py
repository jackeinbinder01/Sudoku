import pygame
from src.resources import settings as s


class GameBoard:
    def __init__(self, game_window):
        self.game_window = game_window
        self.grid_size = s.GRID_SIZE
        self.cell_size = s.CELL_SIZE
        self.x = s.GAME_BOARD_X
        self.y = s.GAME_BOARD_Y
        self.draw_grid()

    def draw_grid(self):

        for i in range(10):
            x = self.x + i * self.cell_size
            y = self.y + i * self.cell_size

            # thick lines for 3x3 boxes
            if i % 3 == 0:
                pygame.draw.line(self.game_window, s.WHITE, (x, self.y), (x, 514), 4)
                pygame.draw.line(self.game_window, s.WHITE, (self.x, y), (505, y), 4)
            # thin lines otherwise
            else:
                pygame.draw.line(self.game_window, s.WHITE, (x, self.y + 3), (x, 514), 1)
                pygame.draw.line(self.game_window, s.WHITE, (self.x + 3, y), (505, y), 1)
