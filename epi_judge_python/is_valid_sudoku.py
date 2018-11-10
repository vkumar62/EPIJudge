from test_framework import generic_test

import math
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    # TODO - you fill in here.
    def checker(start_row, start_col, end_row, end_col):
        vals = []
        for i in range(start_row, end_row+1):
            for j in range(start_col, end_col+1):
                if partial_assignment[i][j] != 0:
                    vals.append(partial_assignment[i][j])
        return len(vals) == len(set(vals))

    # row checker
    N = len(partial_assignment)
    sqrt_n = int(math.sqrt(N))
    for i in range(N):
        if not checker(i, 0, i, N-1):
            return False
        if not checker(0, i, N-1, i):
            return False

    for i in range(sqrt_n):
        for j in range(sqrt_n):
            if not checker(i*sqrt_n, j*sqrt_n, (i+1)*sqrt_n - 1, (j+1)*sqrt_n - 1):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
