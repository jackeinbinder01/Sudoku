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
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.grid_size, self.grid_size))

    def get_game_cells(self):
        return self.game_cells

    def get_selected_cell(self):
        for cell in self.game_cells:
            if cell.is_on:
                return cell.get_row_col()
        return None