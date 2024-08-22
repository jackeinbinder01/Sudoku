import pygame
from src.resources.settings import settings as s


class NumberBoard:
    def __init__(self, game_window):
        self.game_window = game_window
        self.x = s.NUMBER_BOARD_X
        self.y = s.NUMBER_BOARD_Y
        self.width, self.height = s.NUMBER_BOARD_SIZE
        self.draw_number_board()

    def draw_number_board(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
