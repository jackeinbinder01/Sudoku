import pygame
from src.resources import settings as s


class NewPuzzleButton:
    def __init__(self, screen, text, num):
        self.screen = screen
        self.text = text
        self.num = num - 1
        self.width, self.height = s.NEW_PUZZLE_BUTTON_SIZE
        self.x = s.NEW_PUZZLE_BUTTON_X + (self.width * self.num)
        self.y = s.NEW_PUZZLE_BUTTON_Y
        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(self.screen, s.WHITE, (self.x, self.y, self.width, self.height), 1)