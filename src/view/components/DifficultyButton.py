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
        self.on = False
        self.pre_selected = pre_selected
        self.draw_button()
        if pre_selected:
            self.highlight_button(s.WHITE)

    def __str__(self):
        return f"{self.text} button"



    def draw_button(self):
        pygame.draw.rect(self.game_window, s.WHITE, (self.x, self.y, self.width, self.height), 1)
        self.draw_text(self.text, s.WHITE)

    def draw_text(self, text, color):
        font = pygame.font.Font(None, 18)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=self.get_middle_x_y())

        self.game_window.blit(text_surface, text_rect)

    def get_middle_x_y(self):
        return self.x + (self.width / 2), self.y + (self.height / 2)

    def is_clicked(self, position):
        x, y = position
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def toggle_highlight(self):
        if self.on:
            self.highlight_button()
        else:
            self.unhighlight_button()

    def highlight_button(self, color=s.HIGHLIGHT):
        pygame.draw.rect(self.game_window, color, (self.x, self.y, self.width, self.height))
        self.draw_text(self.text, s.BLACK)

    def unhighlight_button(self):
        pygame.draw.rect(self.game_window, s.BLACK, (self.x, self.y, self.width, self.height))
        self.draw_button()
        if self.pre_selected:
            self.highlight_button(s.WHITE)

    def on_click(self):
        return self.click() if not self.on else self.unclick()

    def click(self):
        self.on = True
        self.toggle_highlight()
        return f"'{self.text}' button clicked on"

    def unclick(self):
        self.on = False
        self.toggle_highlight()
        return f"'{self.text}' button clicked off"

    def set_pre_selected(self):
        self.pre_selected = True

    def is_pre_selected(self):
        return self.pre_selected

    def is_on(self):
        return self.on
