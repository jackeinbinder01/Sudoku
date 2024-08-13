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

        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.draw_text()

    def draw_text(self):
        font = pygame.font.Font(None, 18)
        text_surface = font.render(self.text, True, s.WHITE)

        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)


