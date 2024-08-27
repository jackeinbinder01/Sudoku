import random


class Puzzle:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.puzzle = []
        self.generate_puzzle()

    def get_puzzle(self):
        return self.puzzle

    def generate_puzzle(self):
        self.puzzle = [[0 for i in range(9)] for j in range(9)]
        self.solve_puzzle()

    def generate_n_puzzles(self, n):
        self.puzzle = [[0 for i in range(9)] for j in range(9)]
        for i in range(n):
            self.solve_puzzle()

    def pretty_print(self):
        for i in range(len(self.puzzle)):
            print(self.puzzle[i])

    def get_value_at(self, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        value_at_row_col = self.puzzle[row][col]
        return value_at_row_col

    def get_values_in_row(self, row):
        if not (0 <= row < 9):
            raise IndexError("row cannot be less than 0 or exceed 8")
        values_in_row = set(self.puzzle[row])
        return values_in_row

    def get_values_in_col(self, col):
        if not (0 <= col < 9):
            raise IndexError("col cannot be less than 0 or exceed 8")
        values_in_col = set([self.puzzle[i][col] for i in range(9)])
        return values_in_col

    def get_values_in_square(self, square):
        if not (1 <= square <= 9):
            raise IndexError("row and col cannot be less than 1 or exceed 9")
        row_start = (square - 1) // 3 * 3
        col_start = (square - 1) % 3 * 3
        values = set(self.puzzle[row_start + i][col_start + j] for i in range(3) for j in range(3))
        return values

    def get_square_from_row_col(self, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be negative or exceed 8")
        square = ((row // 3) * 3) + (col // 3) + 1
        return square

    def get_candidates(self, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        candidates = set([i for i in range(9) if self.is_valid_move(i, row, col)])
        return candidates

    def is_valid_move(self, num, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        if not (1 <= num <= 9):
            raise IndexError("num cannot be less than 1 or exceed 9")
        if all([self.is_valid_in_row(num, row), self.is_valid_in_col(num, col),
                self.is_valid_in_square(num, row, col)]):
            return True
        return False

    def is_valid_in_row(self, num, row):
        if not (0 <= row < 9):
            raise IndexError("row cannot be less than 0 or exceed 8")
        if not (1 <= num <= 9):
            raise IndexError("num cannot be less than 1 or exceed 9")
        for i in range(9):
            if self.puzzle[row][i] == num:
                return False
        return True

    def is_valid_in_col(self, num, col):
        if not (0 <= col < 9):
            raise IndexError("col cannot be less than 0 or exceed 8")
        if not (1 <= num <= 9):
            raise IndexError("num cannot be less than 1 or exceed 9")
        for i in range(9):
            if self.puzzle[i][col] == num:
                return False
        return True

    def is_valid_in_square(self, num, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        if not (1 <= num <= 9):
            raise IndexError("num cannot be less than 1 or exceed 9")
        num_square = self.get_square_from_row_col(row, col)
        values_in_num_square = self.get_values_in_square(num_square)
        if num in values_in_num_square:
            return False
        return True

    def is_solved(self):
        answer_key = set(range(1, 10))
        for i in range(9):
            if not all([self.get_values_in_row(i) == answer_key,
                        self.get_values_in_col(i) == answer_key,
                        self.get_values_in_square(i + 1) == answer_key]):
                return False
        return True

    def solve_puzzle(self):
        # by backtracking
        for row in range(9):
            for col in range(9):
                if self.get_value_at(row, col) == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid_move(num, row, col):
                            self.set_number_in_cell(num, row, col)
                            if self.solve_puzzle():
                                return True
                            self.set_number_in_cell(0, row, col)
                    return False
        return True

    def set_number_in_cell(self, num, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        if not (0 <= num <= 9):
            raise IndexError("num cannot be less than 0 or exceed 9")
        self.puzzle[row][col] = num

    def has_one_solution(self):
        pass


def main():
    pass

if __name__ == "__main__":
    main()
