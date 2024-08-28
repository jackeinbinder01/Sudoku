def get_values_in_square(puzzle, square):
    if not (1 <= square <= 9):
        raise IndexError("row and col cannot be less than 1 or exceed 9")
    row_start = (square - 1) // 3 * 3
    col_start = (square - 1) % 3 * 3
    values = list(puzzle[row_start + i][col_start + j] for i in range(3) for j in range(3))
    return values


def main():
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print(get_values_in_square(puzzle, 1))


if __name__ == '__main__':
    main()
