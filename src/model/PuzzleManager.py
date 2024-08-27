from src.model.Puzzle import Puzzle


class PuzzleManager:
    def __init__(self):
        self.current_puzzle = None

    def generate_puzzle(self, difficulty):
        self.current_puzzle = Puzzle(difficulty)

    def get_current_puzzle(self):
        if self.current_puzzle is None:
            raise ValueError("Sudoku puzzle has not yet been generated")
        return self.current_puzzle
