import pygame
from resources import settings as s


class NumberBoard:
    def __init__(self, game_window):
        self.game_window = game_window
        self.x = s.X_PADDING * 2 + s.GRID_SIZE
        self.y = s.Y_PADDING + s.DIFFICULTY_BUTTON_HEIGHT + 10 + s.CLOCK_HEIGHT + 10 + s.MODE_BUTTON_HEIGHT + 10
        self.width, self.height = s.NUMBER_BOARD_SIZE
        self.draw_numberboard()

    def draw_numberboard(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
