import pygame
from src.resources import settings as s


class NumberBoard:
    def __init__(self, game_window):
        self.game_window = game_window
        self.x = s.NUMBER_BOARD_X
        self.y = s.NUMBER_BOARD_Y
        self.width, self.height = s.NUMBER_BOARD_SIZE
        self.draw_numberboard()

    def draw_numberboard(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
