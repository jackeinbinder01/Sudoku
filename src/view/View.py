import pygame

from src.resources import settings as s
from src.view.components.Clock import Clock
from src.view.components.DifficultyButton import DifficultyButton
from src.view.components.GameBoard import GameBoard
from src.view.components.NormalButton import NormalButton
from src.view.components.CandidateButton import CandidateButton
from src.view.components.NewPuzzleButton import NewPuzzleButton
from src.view.components.NumberBoard import NumberBoard
from src.view.components.NumberButton import NumberButton
from src.view.components.PuzzleButton import PuzzleButton

'''
Night mode Sudoku view
'''


class View:

    def __init__(self):
        self.game_window = pygame.display.set_mode(s.SCREEN_SIZE)
        pygame.display.set_caption(s.WINDOW_TITLE)
        pygame.font.init()

        # add components
        self.game_board = GameBoard(self.game_window)

        self.easy_button = DifficultyButton(self.game_window, "Easy", 1)
        self.medium_button = DifficultyButton(self.game_window, "Medium", 2)
        self.hard_button = DifficultyButton(self.game_window, "Hard", 3)
        self.new_puzzle_button = NewPuzzleButton(self.game_window, "New Puzzle", 4)

        self.clock = Clock(self.game_window)
        self.normal_button = NormalButton(self.game_window)
        self.candidate_button = CandidateButton(self.game_window)
        self.number_board = NumberBoard(self.game_window)
        self.number_buttons = [NumberButton(self.game_window, i) for i in range(10)]

        self.reset_puzzle_button = PuzzleButton(self.game_window, "Reset Puzzle", 1)
        self.reveal_cell_button = PuzzleButton(self.game_window, "Reveal Cell", 2)
        self.give_up_button = PuzzleButton(self.game_window, "Give Up", 3)

        self.difficulty_buttons = [
            self.easy_button,
            self.medium_button,
            self.hard_button,
        ]

        self.mode_buttons = [
            self.normal_button,
            self.candidate_button,
        ]

        self.puzzle_buttons = [
            self.reset_puzzle_button,
            self.reveal_cell_button,
            self.give_up_button
        ]

        self.components = {
            self.clock,
            self.new_puzzle_button
        }

        # gameloop cond
        self.running = True

    def display(self):
        while self.running:
            self.handle_events()
            self.update_display()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in self.difficulty_buttons:
                    if button.is_clicked(pos):
                        [each.unclick() for each in self.difficulty_buttons if each.is_on]
                        print(f"[View] - {button.on_click()}")
                for button in self.mode_buttons:
                    if button.is_clicked(pos):
                        print(f"[View] - {button.on_click()}")
                for button in self.number_buttons:
                    if button.is_clicked(pos):
                        print(f"[View] - {button.on_click()}")
                for button in self.puzzle_buttons:
                    if button.is_clicked(pos):
                        print(f"[View] - {button.on_click()}")



                for component in self.components:
                    if component.is_clicked(pos):
                        print(f"[View] - {component.on_click()}")
                for cell in self.game_board.get_game_cells():
                    if cell.is_clicked(pos):
                        print(f"[View] - {cell.on_click()}")

    def update_display(self):
        pygame.display.flip()


'''
Test Main
'''


def main():
    view = View()
    view.display()


if __name__ == '__main__':
    main()
