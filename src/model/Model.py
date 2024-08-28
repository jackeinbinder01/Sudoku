from src.model.Puzzle import Puzzle

'''
Sudoku puzzle model
'''


class Model:
    def __init__(self):
        self.DEFAULT_DIFFICULTY = "easy"
        self.puzzle = Puzzle(self.DEFAULT_DIFFICULTY)

    def get_new_puzzle(self, difficulty=None):
        if not difficulty:
            difficulty = self.DEFAULT_DIFFICULTY
        self.puzzle = Puzzle(difficulty)

    def get_puzzle(self):
        return self.puzzle

    def reset_puzzle(self):
        self.puzzle.matrix = [row[:] for row in self.puzzle.initial_matrix]

    def solve_puzzle(self):
        self.puzzle.matrix = [row[:] for row in self.puzzle.solved_matrix]

    def set_number_in_cell(self, num, row, col):
        if self.puzzle.is_valid_move(num, row, col):
            self.puzzle.set_number_in_cell(num, row, col)
        else:
            raise Exception(f"Invalid move num: {num}, row: {row}, col: {col}")

    def is_solved(self):
        return self.puzzle.is_solved()
