import pygame
from src.resources import settings as s
from src.view.components.Clock import Clock
from src.view.components.DifficultyButton import DifficultyButton
from src.view.components.GameBoard import GameBoard
from src.view.components.ModeButton import ModeButton
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
        self.normal_button = ModeButton(self.game_window, "Normal", 1)
        self.candidate_button = ModeButton(self.game_window, "Candidate", 2)
        self.number_board = NumberBoard(self.game_window)
        self.number_buttons = [NumberButton(self.game_window, i) for i in range(10)]

        self.reset_puzzle_button = PuzzleButton(self.game_window, "Reset Puzzle", 1)
        self.reveal_cell_button = PuzzleButton(self.game_window, "Reveal Cell", 2)
        self.give_up_button = PuzzleButton(self.game_window, "Give Up", 3)

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
