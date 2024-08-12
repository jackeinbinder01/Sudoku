import pygame
from resources import settings as s
from view.view_components.Clock import Clock
from view.view_components.DifficultyButton import DifficultyButton
from view.view_components.GameBoard import GameBoard
from view.view_components.ModeButton import ModeButton
from view.view_components.NewPuzzleButton import NewPuzzleButton
from view.view_components.NumberBoard import NumberBoard



class View:

    def __init__(self):
        self.game_window = pygame.display.set_mode(s.SCREEN_SIZE)
        pygame.display.set_caption(s.WINDOW_TITLE)

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
        self.reset_puzzle_button = PuzzleButton(self.game_window, "Reset Puzzle", 1)
        self.reveal_cell_button = PuzzleButton(self.game_window, "Reveal Cell", 1)
        self.give_up_button = PuzzleButton(self.game_window, "Give Up", 1)

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

def main():
    view = View()
    view.display()


if __name__ == '__main__':
    main()
