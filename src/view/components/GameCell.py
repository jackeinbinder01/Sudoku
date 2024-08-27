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
        self.clear_cell = False
        self.user_candidates = set()
        self.auto_candidates = set()
        self.draw_cell()
        self.is_on = False
        self.editable = False
        self.hidden = False

    def __str__(self):
        return f"cell at '{self.get_row_col()}' set to '{self.number}' editable status - {self.editable}"

    def add_candidate(self, candidate):
        if candidate in self.user_candidates:
            self.user_candidates.remove(candidate)
        else:
            self.user_candidates.add(candidate)

    def set_auto_candidates(self, auto_candidates):
        self.auto_candidates = auto_candidates

    def draw_candidate(self, num, color=s.WHITE):
        if num == "X":
            return

        font = pygame.font.Font(None, 16)
        text_surface = font.render(str(num), True, color)

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

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_row_col(self):
        return self.row, self.col

    def get_number(self):
        return self.number

    def set_number(self, number):
        if number == "X":
            self.clear_cell = True
        elif 1 <= number <= 9:
            self.number = number

    def is_editable(self):
        return self.editable

    def set_editable(self, editable=True):
        self.editable = editable

    def is_hidden(self):
        return self.hidden

    def set_hidden(self, hidden=True):
        self.hidden = hidden

    def get_inner_square(self):
        return self.inner_square

    def draw_cell(self, button_color=s.BLACK, text_color=s.WHITE, auto_candidate=False):
        pygame.draw.rect(self.game_window, button_color, (self.x, self.y, self.width, self.height))

        if self.clear_cell and self.user_candidates:
            for each in self.user_candidates:
                self.number = ""
                self.draw_candidate(each, text_color)
                self.clear_cell = False
        elif self.clear_cell:
            self.number = ""
            self.clear_cell = False
            return

        if auto_candidate:
            candidate_list = self.auto_candidates
        else:
            candidate_list = self.user_candidates

        if self.number == "" and candidate_list:
            for candidate in candidate_list:
                self.draw_candidate(candidate, text_color)

        else:
            self.draw_text(str(self.get_number()), text_color)

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
        if not self.hidden:
            self.draw_cell(s.GREY)
        else:
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
