import pygame.draw
from src.resources import settings as s


class ModeButton:
    def __init__(self, game_window, text, num):
        self.game_window = game_window
        self.text = text
        self.num = num - 1
        self.width, self.height = s.MODE_BUTTON_SIZE
        self.x = s.MODE_BUTTON_X + (self.width * self.num)
        self.y = s.MODE_BUTTON_Y
        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
