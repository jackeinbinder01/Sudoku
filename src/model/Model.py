from src.model.Puzzle import Puzzle

'''
Sudoku puzzle model
'''

class Model:
    def __init__(self):
        self.DEFAULT_DIFFICULTY = "easy"
        self.puzzle = Puzzle(self.DEFAULT_DIFFICULTY)
