import time

import pygame.draw
from src.resources.settings import settings as s


class NumberButton:
    def __init__(self, game_window, num):
        self.game_window = game_window
        self.num = num
        self.width, self.height = s.NUMBER_BUTTON_SIZE
        self.x = s.NUMBER_BUTTON_X
        self.y = s.NUMBER_BUTTON_Y
        self.draw_button()
        self.clicked = False

    def __str__(self):
        return f"'{'X' if self.num + 1 == 10 else self.num + 1}' button clicked"

    def draw_button(self):
        row = self.num // 5
        col = self.num % 5

        self.x = s.NUMBER_BUTTON_X + (self.width + s.INX_PADDING) * col
        self.y = s.NUMBER_BUTTON_Y + (self.height + s.INY_BTM_PADDING) * row

        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 3, 10)
        self.draw_number(s.WHITE)

    def draw_number(self, color):
        font = pygame.font.Font(None, 32)

        if self.num + 1 == 10:
            text_surface = font.render("X", True, color)
        else:
            text_surface = font.render(str(self.num + 1), True, color)

        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_number(self):
        if self.num + 1 == 10:
            return 0
        else:
            return self.num + 1

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

    def highlight_button(self):
        pygame.draw.rect(self.game_window, s.HIGHLIGHT, (self.x, self.y, self.width, self.height), 0, 10)
        self.draw_number(s.BLACK)
        pygame.display.update()

    def unhighlight_button(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height), 0, 10)
        self.draw_button()
        pygame.display.update()

    def on_click(self):
        if not self.clicked:
            self.click()
            time.sleep(0.15)
            self.unclick()
        return f"'{'X' if self.num + 1 == 10 else self.num + 1}' button clicked"

    def click(self):
        self.clicked = True
        self.toggle_highlight()

    def unclick(self):
        self.clicked = False
        self.toggle_highlight()
