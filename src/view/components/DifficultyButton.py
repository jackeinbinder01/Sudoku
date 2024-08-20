import pygame
from src.resources import settings as s


class DifficultyButton:
    def __init__(self, game_window, text, num):
        self.game_window = game_window
        self.text = text
        self.num = num - 1
        self.width, self.height = s.DIFFICULTY_BUTTON_SIZE

        self.x = s.DIFFICULTY_BUTTON_X + (self.width * self.num)
        self.y = s.DIFFICULTY_BUTTON_Y

        # Is button currently on
        self.is_on = False

        self.draw_button()

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

    def highlight_button(self):
        pygame.draw.rect(self.game_window, s.HIGHLIGHT, (self.x, self.y, self.width, self.height))
        self.draw_text(s.BLACK)

    def unhighlight_button(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.draw_text(s.WHITE)

    def on_click(self):
        return self.click() if not self.is_on else self.unclick()

    def click(self):
        self.is_on = True
        self.highlight_button()
        return f"\'{self.text}\' button clicked on"

    def unclick(self):
        self.is_on = False
        self.unhighlight_button()
        return f"\'{self.text}\' button clicked off"