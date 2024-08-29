import random

'''
Sudoku puzzle represented by 2D matrix
'''


class Puzzle:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.matrix = []
        self.solved_matrix = []
        self.initial_matrix = []
        self.invalid_affected_cells = set()
        self.generate_puzzle()

    def get_difficulty(self):
        return self.difficulty

    def get_matrix(self, matrix="matrix", flattened=False):
        match matrix:
            case "matrix":
                return self.get_flattened_matrix(self.matrix) if flattened else self.matrix
            case "initial_matrix":
                return self.get_flattened_matrix(self.initial_matrix) if flattened else self.initial_matrix
            case "solved_matrix":
                return self.get_flattened_matrix(self.solved_matrix) if flattened else self.solved_matrix
            case _:
                raise ValueError(f"Invalid matrix '{matrix}'")

    def get_flattened_matrix(self, matrix=None):
        return [value for row in (self.matrix if matrix is None else matrix) for value in row]

    def hide_values(self):
        match self.difficulty.lower():
            case "easy":
                values_to_hide = random.randint(41, 46)
            case "medium":
                values_to_hide = random.randint(47, 51)
            case "hard":
                values_to_hide = random.randint(52, 56)
            case _:
                raise ValueError(f"Invalid difficulty: {self.difficulty}")

        hidden_values = 0
        while hidden_values < values_to_hide:
            random_row, random_col = random.randint(0, 8), random.randint(0, 8)
            if self.matrix[random_row][random_col] != 0:
                self.matrix[random_row][random_col] = 0
                hidden_values += 1

    def generate_puzzle(self):
        self.matrix = [[0 for _ in range(9)] for _ in range(9)]
        self.solve_puzzle()
        self.solved_matrix = [row[:] for row in self.matrix]
        self.hide_values()
        self.initial_matrix = [row[:] for row in self.matrix]

    def generate_n_puzzles(self, n):
        self.matrix = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(n):
            self.solve_puzzle()

    def pretty_print(self):
        [print(self.matrix[i]) for i in range(len(self.matrix))]

    def get_value_at(self, row, col, matrix=None):
        if matrix is None:
            matrix = self.matrix
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        value_at_row_col = matrix[row][col]
        return value_at_row_col

    def get_row(self, row):
        if not (0 <= row < 9):
            raise IndexError("row cannot be less than 0 or exceed 8")
        return self.matrix[row]

    def get_col(self, col):
        if not (0 <= col < 9):
            raise IndexError("col cannot be less than 0 or exceed 8")
        return [self.matrix[i][col] for i in range(9)]

    def get_square(self, square):
        if not (1 <= square <= 9):
            raise IndexError("row and col cannot be less than 1 or exceed 9")
        row_start = (square - 1) // 3 * 3
        col_start = (square - 1) % 3 * 3
        return list(self.matrix[row_start + i][col_start + j] for i in range(3) for j in range(3))

    def get_values_in_row(self, row):
        return set(self.get_row(row))

    def get_values_in_col(self, col):
        return set(self.get_col(col))

    def get_values_in_square(self, square):
        return set(self.get_square(square))

    def get_square_from_row_col(self, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be negative or exceed 8")
        square = ((row // 3) * 3) + (col // 3) + 1
        return square

    def get_candidates(self, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        candidates = set([i for i in range(1, 10) if self.is_valid_move(i, row, col)])
        return candidates

    def is_valid_move(self, num, row, col):
        if num == 0:
            return True
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        if not (0 <= num <= 9):
            raise IndexError("num cannot be less than 0 or exceed 9")
        return (self.is_valid_in_row(num, row) and
                self.is_valid_in_col(num, col) and
                self.is_valid_in_square(num, row, col))

    def find_invalid_affected_cells(self):
        self.invalid_affected_cells = set()
        for row in range(len(self.matrix)):
            self.invalid_affected_cells.update(self.get_duped_cells_in_row(row))
        for col in range(len(self.matrix[0])):
            self.invalid_affected_cells.update(self.get_duped_cells_in_col(col))
        for row in range(0, len(self.matrix), 3):
            for col in range(0, len(self.matrix[0]), 3):
                self.invalid_affected_cells.update(self.get_duped_cells_in_square(row, col))

    def get_duped_cells_in_row(self, row):
        duped_cells = set()
        cells_in_row = self.get_row(row)
        for col_idx, num in enumerate(cells_in_row):
            if num > 0 and cells_in_row.count(num) > 1:
                duped_cells.add((row, col_idx))
        return duped_cells

    def get_duped_cells_in_col(self, col):
        duped_cells = set()
        cells_in_col = self.get_col(col)
        for row_idx, num in enumerate(cells_in_col):
            if num > 0 and cells_in_col.count(num) > 1:
                duped_cells.add((row_idx, col))
        return duped_cells

    def get_duped_cells_in_square(self, row, col):
        duped_cells = set()
        square = self.get_square_from_row_col(row, col)
        cells_in_square = self.get_square(square)
        for num in self.get_square(square):
            if num > 0 and cells_in_square.count(num) > 1:
                if self.get_value_at(row, col) == num:
                    duped_cells.add((row, col))
        return duped_cells

    def get_invalid_affected_cells(self):
        return self.invalid_affected_cells

    def is_valid_in_row(self, num, row):
        if not (0 <= row < 9):
            raise IndexError("row cannot be less than 0 or exceed 8")
        if not (1 <= num <= 9):
            raise IndexError("num cannot be less than 1 or exceed 9")
        return not any(self.matrix[row][i] == num for i in range(9))

    def is_valid_in_col(self, num, col):
        if not (0 <= col < 9):
            raise IndexError("col cannot be less than 0 or exceed 8")
        if not (1 <= num <= 9):
            raise IndexError("num cannot be less than 1 or exceed 9")
        return not any(self.matrix[i][col] == num for i in range(9))

    def is_valid_in_square(self, num, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            raise IndexError("row and col cannot be less than 0 or exceed 8")
        if not (1 <= num <= 9):
            raise IndexError("num cannot be less than 1 or exceed 9")
        num_square = self.get_square_from_row_col(row, col)
        values_in_num_square = self.get_values_in_square(num_square)
        return num not in values_in_num_square

    def is_solved(self):
        answer_key = set(range(1, 10))
        return all(
            self.get_values_in_row(i) == answer_key and
            self.get_values_in_col(i) == answer_key and
            self.get_values_in_square(i + 1) == answer_key
            for i in range(9)
        )

    def solve_puzzle(self):
        # solve by backtracking
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
        try:
            if not (0 <= row < 9 and 0 <= col < 9):
                raise IndexError("row and col cannot be less than 0 or exceed 8")
            if not (0 <= num <= 9):
                raise ValueError("num cannot be less than 0 or exceed 9")
            self.matrix[row][col] = num
        except Exception as e:
            print(f"Error in set_number_in_cell(): {e}")

    def has_one_solution(self):
        pass
