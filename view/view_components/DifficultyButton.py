import pygame
from resources import settings as s


class DifficultyButton:
    def __init__(self, screen, text, num):
        self.screen = screen
        self.text = text
        self.num = num - 1
        self.width, self.height = s.DIFFICULTY_BUTTON_SIZE

        self.x = s.X_PADDING * 2 + s.GRID_SIZE
        self.y = s.Y_PADDING

        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(self.screen, s.WHITE, (self.x + (self.width * self.num), self.y, self.width, self.height), 1)