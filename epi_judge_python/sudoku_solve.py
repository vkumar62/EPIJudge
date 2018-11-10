import copy
import functools
import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import math
def solve_sudoku(partial_assignment):
    # TODO - you fill in here.
    def solve_helper(i, j):
        if j == N:
            i = i+1
            j = 0
            if i == N:
                # All complete
                return True
        if partial_assignment[i][j] != 0:
            return solve_helper(i, j+1)

        for val in range(1, N+1):
            if valid_assign(i,j,val):
                partial_assignment[i][j] = val
                if solve_helper(i, j+1):
                    return True
        #no valid assignments found, backtrack
        partial_assignment[i][j] = 0
        return False

    def valid_assign(x, y, val):
        #Check if val can be assigned at i,j
        #col check
        for j in range(N):
            if partial_assignment[x][j] == val:
                return False
        for i in range(N):
            if partial_assignment[i][y] == val:
                return False
        #grid check
        for i in range((x//sqrt_n) * sqrt_n, (x//sqrt_n) * sqrt_n + sqrt_n):
            for j in range((y//sqrt_n)*sqrt_n, (y//sqrt_n)*sqrt_n+sqrt_n):
                if partial_assignment[i][j] == val:
                    return False
        return True

    N = len(partial_assignment)
    sqrt_n = int(math.sqrt(N))
    return solve_helper(0,0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))

    for i in range(len(solved)):
        assert_unique_seq(solved[i])
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sudoku_solve.py", 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
