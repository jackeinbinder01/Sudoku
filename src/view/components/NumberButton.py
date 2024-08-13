import pygame.draw
from src.resources import settings as s


class NumberButton:
    def __init__(self, game_window, num):
        self.game_window = game_window
        self.num = num
        self.width, self.height = s.NUMBER_BUTTON_SIZE
        self.x = s.NUMBER_BUTTON_X
        self.y = s.NUMBER_BUTTON_Y
        self.draw_button()

    def draw_button(self):
        row = self.num // 5
        col = self.num % 5

        x = self.x + (self.width + s.INX_PADDING) * col
        y = self.y + (self.height + s.INY_BTM_PADDING) * row

        pygame.draw.rect(self.game_window, s.WHITE, (x, y, self.width, self.height), 3, 10)
