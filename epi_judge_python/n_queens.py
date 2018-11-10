from test_framework import generic_test


def n_queens(n):

    def is_valid_placement(row, col):
        for i in range(0, row):
            #diff =  abs(col - placement[i])
            if col == placement[i]:
                return False
            #Diagonal check 
            if col == placement[i]+row-i:
                return False
            if col == placement[i]-(row-i):
                return False
            #if diff == 0 or diff == (row - i):
            #    return False
        return True

    def n_queens_helper(row):
        if row == n:
            result.append(placement[:])
            return

        for col in range(n):
            #placement[row] = col
            if is_valid_placement(row, col):
                placement[row] = col 
                n_queens_helper(row+1)

    placement = [None] * n
    result = []

    n_queens_helper(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
