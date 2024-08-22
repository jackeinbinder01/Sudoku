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

        self.rise = 4
        self.run = 4

        self.x = s.GAME_BOARD_X + 4 + (self.width * self.col + (1 * self.col))
        self.y = s.GAME_BOARD_Y + 4 + (self.height * self.row + (1 * self.row))

        if self.row >= 3:
            self.y = self.y + 3
        if self.row >= 6:
            self.y = self.y + 3

        if self.col >= 3:
            self.x = self.x + 3
        if self.col >= 6:
            self.x = self.x + 3

        self.number = None
        self.inner_square = ((self.row // 3) * 3) + ((self.col // 3) + 1)

        self.draw_cell()

        self.is_on = False

        self.candidates = []
        self.display_number_error()

    def display_number_error(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        error_icon_path = os.path.join(current_dir + "/resources/images/number_error_icon.png")
        error_icon = pygame.image.load(error_icon_path)

        error_cell_size = self.width / 3

        x = self.x + error_cell_size / 2 + (error_cell_size * 2) - 10
        y = self.y + error_cell_size / 2 + (error_cell_size * 2) - 10

        self.game_window.blit(error_icon, (x, y))

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

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def get_row_col(self):
        return self.row + 1, chr(self.col + ord('a'))

    def get_number(self):
        return self.number

    def get_inner_square(self):
        return self.inner_square

    def set_number(self, number):
        if 1 <= number <= 9:
            self.number = number

    def draw_cell(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        # self.draw_text(s.WHITE)

    def draw_text(self, color):
        font = pygame.font.Font(None, 32)
        text_surface = font.render(str(self.get_inner_square()), True, color)

        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def highlight_button(self):
        pygame.draw.rect(self.game_window, s.HIGHLIGHT, (self.x, self.y, self.width, self.height))
        self.draw_text(s.BLACK)

    def unhighlight_button(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        self.draw_text(s.WHITE)

    def on_click(self):
        return self.click() if not self.is_on else self.unclick()

    def click(self):
        self.is_on = True
        self.highlight_button()
        return f"\'{self.get_row_col()}\' cell clicked on"

    def unclick(self):
        self.is_on = False
        self.unhighlight_button()
        return f"\'{self.get_row_col()}\' cell clicked off"
