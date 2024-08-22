import pygame
from src.resources.settings import settings as s


class DifficultyButton:

    def __init__(self, game_window, text, num, pre_selected=False):
        self.game_window = game_window
        self.text = text
        self.num = num - 1
        self.width, self.height = s.DIFFICULTY_BUTTON_SIZE

        self.x = s.DIFFICULTY_BUTTON_X + (self.width * self.num)
        self.y = s.DIFFICULTY_BUTTON_Y

        self.is_on = False
        self.pre_selected = pre_selected

        self.draw_button()

        if pre_selected:
            self.highlight_button(s.WHITE)

    def draw_button(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.draw_text(s.WHITE)

    def draw_text(self, color):
        font = pygame.font.Font(None, 18)
        text_surface = font.render(self.text, True, color)

        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def highlight_button(self, color):
        pygame.draw.rect(self.game_window, color, (self.x, self.y, self.width, self.height))
        self.draw_text(s.BLACK)

    def unhighlight_button(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.draw_text(s.WHITE)
        if self.pre_selected:
            self.highlight_button(s.WHITE)

    def on_click(self):
        return self.click() if not self.is_on else self.unclick()

    def click(self):
        self.is_on = True
        self.highlight_button(s.HIGHLIGHT)
        return f"\'{self.text}\' button clicked on"

    def unclick(self):
        self.is_on = False
        self.unhighlight_button()
        return f"\'{self.text}\' button clicked off"

    def set_pre_selected(self):
        self.pre_selected = True

    def is_pre_selected(self):
        return self.pre_selected

    def is_on(self):
        return self.is_on
