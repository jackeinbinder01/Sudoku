import time

import pygame
from src.resources.settings import settings as s


class Clock:
    def __init__(self, game_window):
        self.game_window = game_window
        self.width, self.height = s.CLOCK_SIZE
        self.x = s.CLOCK_X
        self.y = s.CLOCK_Y
        self.paused = False
        self.start_time = time.time()
        self.elapsed_time = 0
        self.draw_clock()

    def __str__(self):
        return f'Clock clicked'

    def is_paused(self):
        return self.paused

    def draw_clock(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.display_time()

    def get_time(self, long_format=False):
        current_time = time.time()
        if not self.paused:
            self.elapsed_time = current_time - self.start_time

        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)

        if not long_format:
            if hours > 0:
                return f"{hours}:{minutes:02}:{seconds:02}"
            else:
                return f"{minutes:02}:{seconds:02}"
        else:
            if hours > 0:
                return f"{hours} {"hour" if hours == 1 else "hours"}, {minutes} {"minute" if minutes == 1 else "minutes"} and {seconds} {"second" if seconds == 1 else "seconds"}"
            elif 60 > minutes > 0:
                return f"{minutes} {"minute" if minutes == 1 else "minutes"} and {seconds} {"second" if seconds == 1 else "seconds"}"
            else:
                return f"{seconds} {"second" if seconds == 1 else "seconds"}"

    def display_time(self):
        font = pygame.font.Font(None, 80)
        text_surface = font.render(self.get_time(), True, s.WHITE)
        text_rect = text_surface.get_rect(center=self.get_middle_x_y())
        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def on_click(self):
        return self.pause() if not self.paused else self.resume()

    def pause(self):
        self.paused = True
        self.start_time = time.time() - self.elapsed_time
        return "'Clock' paused"

    def resume(self):
        self.paused = False
        self.start_time = time.time() - self.elapsed_time
        return "'Clock' resumed"
