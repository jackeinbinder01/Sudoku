import pygame.draw

from resources import settings as s


class ModeButton:
    def __init__(self, game_window, text, num):
        self.game_window = game_window
        self.text = text
        self.num = num - 1

        self.x = s.X_PADDING * 2 + s.GRID_SIZE
        self.y = s.Y_PADDING + s.DIFFICULTY_BUTTON_HEIGHT + 10 + s.CLOCK_HEIGHT + 10
        self.width, self.height = s.MODE_BUTTON_SIZE
        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x + (self.width * self.num), self.y, self.width, self.height), 1)
