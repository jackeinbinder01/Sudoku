from src.model.Puzzle import Puzzle

'''
Sudoku puzzle model
'''


class Model:
    def __init__(self):
        self.DEFAULT_DIFFICULTY = "easy"
        self.puzzle = Puzzle(self.DEFAULT_DIFFICULTY)

    def get_new_puzzle(self, difficulty):
        self.puzzle = Puzzle(difficulty)

    def get_puzzle(self):
        return self.puzzle

    def is_solved(self):
        return self.puzzle.is_solved()
