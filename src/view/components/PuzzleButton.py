import pygame.draw
from src.resources import settings as s


class PuzzleButton:
    def __init__(self, game_window, text, num):
        self.game_window = game_window
        self.text = text
        self.num = num - 1
        self.width, self.height = s.PUZZLE_BUTTON_SIZE
        self.x = s.PUZZLE_BUTTON_X + (self.width + s.IB_PADDING) * self.num
        self.y = s.PUZZLE_BUTTON_Y

        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
