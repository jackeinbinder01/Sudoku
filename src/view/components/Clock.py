import pygame
from src.resources import settings as s


class Clock:
    def __init__(self, game_window):
        self.game_window = game_window
        self.width, self.height = s.CLOCK_SIZE
        self.x = s.CLOCK_X
        self.y = s.CLOCK_Y
        self.draw_clock()

    def draw_clock(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
