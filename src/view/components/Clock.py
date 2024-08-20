import pygame
from src.resources import settings as s


class Clock:
    def __init__(self, game_window):
        self.game_window = game_window
        self.width, self.height = s.CLOCK_SIZE
        self.x = s.CLOCK_X
        self.y = s.CLOCK_Y
        self.draw_clock()
        self.is_paused = False

    def draw_clock(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def on_click(self):
        return self.pause() if not self.is_paused else self.resume()

    def pause(self):
        self.is_paused = True
        return "'Clock' paused"

    def resume(self):
        self.is_paused = False
        return "'Clock' resumed"
