import os

import pygame

from src.resources.settings import settings as s


class GameCell:
    def __init__(self, game_window, num):
        self.game_window = game_window
        self.num = num
        self.row = (num // 9)
        self.col = num % 9
        self.width = self.height = s.CELL_SIZE
        self.x = s.GAME_BOARD_X + s.THICK_BORDER_WEIGHT + (
                    self.width * self.col + (s.THIN_BORDER_WEIGHT * self.col)) + (self.col // 3) * 3
        self.y = s.GAME_BOARD_Y + s.THICK_BORDER_WEIGHT + (
                    self.height * self.row + (s.THIN_BORDER_WEIGHT * self.row)) + (self.row // 3) * 3
        self.number = ""
        self.inner_square = ((self.row // 3) * 3) + ((self.col // 3) + 1)
        self.draw_cell()
        self.is_on = False
        self.candidates = []

    def __str__(self):
        return f"cell at '{self.get_row_col()}' set to '{self.number}'"

    def draw_candidate(self, num):
        font = pygame.font.Font(None, 16)
        text_surface = font.render(str(num), True, s.WHITE)

        candidate_cell_size = self.width / 3

        row = (num - 1) // 3
        col = (num - 1) % 3

        x = self.x + candidate_cell_size / 2 + (candidate_cell_size * col)
        y = self.y + candidate_cell_size / 2 + (candidate_cell_size * row)

        text_rect = text_surface.get_rect(center=(x, y))

        self.game_window.blit(text_surface, text_rect)

    def display_number_error(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        error_icon_path = os.path.join(current_dir + "/resources/images/number_error_icon.png")
        error_icon = pygame.image.load(error_icon_path)

        error_cell_size = self.width / 3

        x = self.x + error_cell_size / 2 + (error_cell_size * 2) - 10
        y = self.y + error_cell_size / 2 + (error_cell_size * 2) - 10

        self.game_window.blit(error_icon, (x, y))

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def get_row_col(self):
        return self.row + 1, chr(self.col + ord('a'))

    def get_number(self):
        return self.number

    def set_number(self, number):
        if 1 <= number <= 9:
            self.number = number

    def get_inner_square(self):
        return self.inner_square

    def draw_cell(self, button_color=s.BLACK, text_color=s.WHITE):
        pygame.draw.rect(self.game_window, button_color, (self.x, self.y, self.width, self.height))
        self.draw_text(self.get_number(), text_color)

    def draw_text(self, text, color):
        font = pygame.font.Font(None, 32)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def toggle_highlight(self):
        if self.is_on:
            self.highlight_button()
        else:
            self.unhighlight_button()

    def highlight_button(self, color=s.HIGHLIGHT):
        self.draw_cell(color, s.BLACK)

    def unhighlight_button(self):
        self.draw_cell()

    def on_click(self):
        return self.click() if not self.is_on else self.unclick()

    def click(self):
        self.is_on = True
        self.toggle_highlight()
        return f"'{self.get_row_col()}' cell clicked on"

    def unclick(self):
        self.is_on = False
        self.toggle_highlight()
        return f"'{self.get_row_col()}' cell clicked off"
