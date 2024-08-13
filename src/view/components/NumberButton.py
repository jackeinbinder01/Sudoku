import pygame.draw
from src.resources import settings as s


class NumberButton:
    def __init__(self, game_window, num):
        self.game_window = game_window
        self.num = num
        self.width, self.height = s.NUMBER_BUTTON_SIZE
        self.x = s.NUMBER_BUTTON_X
        self.y = s.NUMBER_BUTTON_Y
        self.draw_button()

    def draw_button(self):
        row = self.num // 5
        col = self.num % 5

        self.x = s.NUMBER_BUTTON_X + (self.width + s.INX_PADDING) * col
        self.y = s.NUMBER_BUTTON_Y + (self.height + s.INY_BTM_PADDING) * row

        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 3, 10)
        self.draw_number()

    def draw_number(self):
        font = pygame.font.Font(None, 32)

        if self.num + 1 == 10:
            text_surface = font.render("X", True, s.WHITE)
        else:
            text_surface = font.render(str(self.num + 1), True, s.WHITE)

        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)
