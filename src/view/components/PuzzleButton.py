import time
import pygame.draw
from src.resources import settings as s


class PuzzleButton:
    def __init__(self, game_window, text, num):
        self.game_window = game_window
        self.text = text
        self.num = num - 1
        self.width, self.height = s.PUZZLE_BUTTON_SIZE
        self.x = s.PUZZLE_BUTTON_X + (self.width + s.IB_PADDING) * self.num
        self.y = s.PUZZLE_BUTTON_Y

        self.draw_button()
        self.clicked = False

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
        pygame.display.update()

    def unhighlight_button(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.draw_text(s.WHITE)
        pygame.display.update()

    def on_click(self):
        if not self.clicked:
            self.click()
            time.sleep(0.15)
            self.unclick()
        return f"'{self.text}' button clicked"

    def click(self):
        self.clicked = True
        self.highlight_button()

    def unclick(self):
        self.clicked = False
        self.unhighlight_button()
