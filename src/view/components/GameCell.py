import pygame

from src.resources import settings as s


class GameCell:
    def __init__(self, game_window, num):
        self.game_window = game_window
        self.num = num

        self.row = (num // 9)
        self.col = num % 9
        self.width = self.height = s.CELL_SIZE

        self.x = s.GAME_BOARD_X + (self.width * self.col)
        self.y = s.GAME_BOARD_Y + (self.height * self.row)

        self.number = None
        self.inner_square = ((self.row // 3) * 3) + ((self.col // 3) + 1)

        self.cell_highlighted = False

        self.draw_text(s.WHITE)

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def on_click(self):
        if self.cell_highlighted:
            self.unhighlight_cell()
        else:
            self.highlight_cell()
        return f"{self.get_row_col()} cell clicked"

    def get_row_col(self):
        return self.row + 1, chr(self.col + ord('a'))

    def get_number(self):
        return self.number

    def get_inner_square(self):
        return self.inner_square

    def set_number(self, number):
        if 1 <= number <= 9:
            self.number = number

    def highlight_cell(self):
        pygame.draw.rect(self.game_window, s.HIGHLIGHT, (self.x, self.y, self.width, self.height))
        self.draw_text(s.BLACK)
        self.cell_highlighted = True

    def unhighlight_cell(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        self.draw_text(s.WHITE)
        self.cell_highlighted = False

    def draw_text(self, color):
        font = pygame.font.Font(None, 32)
        text_surface = font.render(str(self.get_inner_square()), True, color)

        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def is_highlighted(self):
        return self.cell_highlighted
