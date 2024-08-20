import pygame
from src.resources import settings as s
from src.view.components.GameCell import GameCell


class GameBoard:
    def __init__(self, game_window):
        self.game_window = game_window
        self.grid_size = s.GRID_SIZE
        self.cell_size = s.CELL_SIZE
        self.x = s.GAME_BOARD_X
        self.y = s.GAME_BOARD_Y
        self.draw_grid()

        self.game_cells = [GameCell(self.game_window, i) for i in range(9 * 9)]

    def draw_grid(self):

        for i in range(10):
            x = self.x + i * self.cell_size
            y = self.y + i * self.cell_size

            # Thick lines for 3x3 boxes
            if i % 3 == 0:
                pygame.draw.line(self.game_window, s.WHITE, (x, self.y), (x, self.y + self.grid_size), 4)
                pygame.draw.line(self.game_window, s.WHITE, (self.x, y), (self.x + self.grid_size, y), 4)
            # Thin lines otherwise
            else:
                pygame.draw.line(self.game_window, s.WHITE, (x, self.y), (x, self.y + self.grid_size), 1)
                pygame.draw.line(self.game_window, s.WHITE, (self.x, y), (self.x + self.grid_size, y), 1)

    def get_game_cells(self):
        return self.game_cells

    def get_selected_cell(self):
        for cell in self.game_cells:
            if cell.is_on:
                return cell.get_row_col()
        return None