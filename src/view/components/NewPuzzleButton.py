import time

import pygame
from src.resources.settings import settings as s


class NewPuzzleButton:
    def __init__(self, game_window, text, num):
        self.game_window = game_window
        self.text = text
        self.num = num - 1
        self.width, self.height = s.NEW_PUZZLE_BUTTON_SIZE
        self.x = s.NEW_PUZZLE_BUTTON_X + (self.width * self.num)
        self.y = s.NEW_PUZZLE_BUTTON_Y
        self.draw_button()
        self.clicked = False
        self.is_armed = False

    def draw_button(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.draw_text(self.text, s.WHITE)

    def draw_text(self, text, color):
        font = pygame.font.Font(None, 18)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def toggle_highlight(self):
        if self.clicked:
            self.highlight_button()
        else:
            self.unhighlight_button()

    def highlight_button(self, button_color=s.HIGHLIGHT, text_color=s.BLACK):
        pygame.draw.rect(self.game_window, button_color, (self.x, self.y, self.width, self.height))
        self.draw_text(self.text, text_color)

    def unhighlight_button(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        self.draw_button()

    def on_click(self):
        if not self.clicked:
            self.click()
            time.sleep(0.15)
            self.unclick()
        return f"'{self.text}' button clicked"

    def click(self):
        self.clicked = True
        self.toggle_highlight()

    def unclick(self):
        self.clicked = False
        self.toggle_highlight()

    def arm_button(self):
        self.is_armed = True
        self.highlight_button(s.RED, s.WHITE)

    def disarm_button(self):
        self.is_armed = False
        self.unhighlight_button()