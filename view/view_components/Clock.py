import pygame

from resources import settings as s


class Clock:
    def __init__(self, game_window):
        self.game_window = game_window
        self.width, self.height = s.CLOCK_SIZE
        self.x = s.X_PADDING * 2 + s.GRID_SIZE
        self.y = s.Y_PADDING + 10 + 30
        self.draw_clock()

    def draw_clock(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
