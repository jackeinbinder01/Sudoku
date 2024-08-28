import pygame

from src.resources.settings import settings as s
from src.view.components.Clock import Clock
from src.view.components.DifficultyButton import DifficultyButton
from src.view.components.GameBoard import GameBoard
from src.view.components.NormalButton import NormalButton
from src.view.components.CandidateButton import CandidateButton
from src.view.components.NewPuzzleButton import NewPuzzleButton
from src.view.components.NumberBoard import NumberBoard
from src.view.components.NumberButton import NumberButton
from src.view.components.PuzzleButton import PuzzleButton
from src.view.components.PopUp import PopUp

'''
Sudoku app view
'''


class View:

    def __init__(self):

        self.game_window = None
        self.game_board = None
        self.easy_button = None
        self.medium_button = None
        self.hard_button = None
        self.new_puzzle_button = None
        self.clock = None
        self.normal_button = None
        self.candidate_button = None
        self.number_board = None
        self.number_buttons = None
        self.reset_puzzle_button = None
        self.reveal_cell_button = None
        self.give_up_button = None

        self.difficulty_buttons = []
        self.mode_buttons = []
        self.puzzle_buttons = []
        self.components = []

        self.reset_display()

        self.winner_popup = None

        self.observer = None

        # gameloop
        self.running = True

    def set_observer(self, observer):
        self.observer = observer

    def notify_observer(self, event, button):
        self.observer.process_events(event, button)

    def set_default_difficulty(self, difficulty):
        if difficulty.lower() in ["easy", "medium", "hard"]:
            self.default_difficulty = difficulty.lower

    def init_game_window(self):
        self.game_window = pygame.display.set_mode(s.SCREEN_SIZE)
        pygame.display.set_caption(s.WINDOW_TITLE)
        pygame.font.init()

    def display(self):
        while self.running:
            self.handle_events()
            self.update_display()

    def reset_display(self, difficulty="easy"):
        self.init_game_window()
        self.init_components(difficulty)
        self.package_components()

        # gameloop
        self.running = True

    def init_components(self, difficulty="easy"):
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

        self.reset_puzzle_button, self.reveal_cell_button, self.give_up_button = (
            PuzzleButton(self.game_window, text, num)
            for text, num in [("Reset Puzzle", 1), ("Reveal Cell", 2), ("Give Up", 3)]
        )

        self.winner_popup = PopUp(self.game_window, "Winner")

    def package_components(self):
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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in self.difficulty_buttons:
                    if button.is_clicked(pos):
                        self.notify_observer("difficulty_button_click", button)
                for button in self.mode_buttons:
                    if button.is_clicked(pos):
                        self.notify_observer("mode_button_click", button)

                for button in self.number_buttons:
                    if button.is_clicked(pos):
                        self.notify_observer("number_button_click", button)
                for button in self.puzzle_buttons:
                    if button.is_clicked(pos):
                        self.notify_observer("puzzle_button_click", button)
                for component in self.components:
                    if component.is_clicked(pos):
                        self.notify_observer("other_component_clicked", component)
                if self.clock.is_clicked(pos):
                    self.notify_observer("clock_click", self.clock)
                if self.new_puzzle_button.is_clicked(pos):
                    self.notify_observer("new_puzzle_button_click", self.new_puzzle_button)
                for cell in self.game_board.get_game_cells():
                    if cell.is_clicked(pos):
                        self.notify_observer("cell_click", cell)

    def update_display(self):
        self.clock.draw_clock()
        pygame.display.flip()

    def get_game_board(self):
        return self.game_board

    def show_winner_popup(self, message):
        pygame.display.flip()
        self.winner_popup = PopUp("Congratulations!", message)
        self.winner_popup.show()
