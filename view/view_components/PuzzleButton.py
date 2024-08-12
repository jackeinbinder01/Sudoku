import pygame.draw


class PuzzleButton:
    def __init__(self, game_window, text, num):
        self.game_window = game_window
        self.text = text
        self.num = num - 1
        self.draw_button()


    def draw_button(self):
        pygame.draw.rect()
