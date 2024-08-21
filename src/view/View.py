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
Sudoku app view
'''


class View:

    def __init__(self):
        self.game_window = pygame.display.set_mode(s.SCREEN_SIZE)
        pygame.display.set_caption(s.WINDOW_TITLE)
        pygame.font.init()

        # add components
        self.game_board = GameBoard(self.game_window)

        self.easy_button = DifficultyButton(self.game_window, "Easy", 1, True)
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

    def reset_display(self, difficulty="easy"):
        self.game_window = pygame.display.set_mode(s.SCREEN_SIZE)
        pygame.display.set_caption(s.WINDOW_TITLE)
        pygame.font.init()

        # add components
        self.game_board = GameBoard(self.game_window)

        self.easy_button, self.medium_button, self.hard_button = (
            DifficultyButton(self.game_window, text, num, difficulty.lower() == key)
            for key, num, text in [("easy", 1, "Easy"), ("medium", 2, "Medium"), ("hard", 3, "Hard")]
        )

        self.new_puzzle_button = NewPuzzleButton(self.game_window, "New Puzzle", 4)

        self.clock = Clock(self.game_window)
        self.normal_button = NormalButton(self.game_window)
        self.candidate_button = CandidateButton(self.game_window)
        self.number_board = NumberBoard(self.game_window)
        self.number_buttons = [NumberButton(self.game_window, i) for i in range(10)]

        self.reset_puzzle_button = PuzzleButton(self.game_window, "New Reset Puzzle", 1)
        self.reveal_cell_button = PuzzleButton(self.game_window, "New Reveal Cell", 2)
        self.give_up_button = PuzzleButton(self.game_window, "New Give Up", 3)

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in self.difficulty_buttons:
                    if button.is_clicked(pos):
                        [each.unclick() for each in self.difficulty_buttons if each.is_on and each != button]
                        print(f"[View] - {button.on_click()}")
                        [self.new_puzzle_button.arm_button() for each in self.difficulty_buttons if each.is_on]

                        if not any([each.is_on for each in self.difficulty_buttons]):
                            self.new_puzzle_button.disarm_button()

                for button in self.mode_buttons:
                    if button.is_clicked(pos):
                        if button == self.normal_button:
                            if self.candidate_button.is_on and not self.candidate_button.auto_candidate:
                                self.candidate_button.unclick()
                            if self.candidate_button.auto_candidate:
                                self.candidate_button.on_click()
                            if self.normal_button.is_on and not self.candidate_button.is_on:
                                break
                        if button == self.candidate_button:
                            if self.normal_button.is_on and not self.candidate_button.auto_candidate:
                                self.normal_button.unclick()
                            if self.candidate_button.is_on:
                                self.normal_button.click()
                            if self.candidate_button.auto_candidate:
                                self.normal_button.unclick()
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
                        [each.unclick() for each in self.game_board.get_game_cells() if each.is_on and each != cell]
                        print(f"[View] - {cell.on_click()}")
                        print(f"[View] - Selected Cell = {self.game_board.get_selected_cell()}")

                if self.new_puzzle_button.is_clicked(pos):
                    self.reset_display()

    def update_display(self):
        self.clock.draw_clock()
        pygame.display.flip()




'''
Test Main
'''


def main():
    view = View()
    view.display()


if __name__ == '__main__':
    main()
