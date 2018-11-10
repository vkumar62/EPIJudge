from test_framework import generic_test


#Time O(nm)
# Space O(nm)
def number_of_ways(n, m):
    # TODO - you fill in here.
    counts = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                counts[i][j] = 1
            else:
                counts[i][j] = counts[i-1][j] + counts[i][j-1]
    return counts[-1][-1]

#Time O(nm)
# Space O(min(n,m))
def number_of_ways(n, m):
    N = min(n,m)
    counts = [0] * N
    counts[0] = 1

    for i in range(max(n,m)):
        for j in range(1, min(n,m)):
            counts[j] += counts[j-1]
    return counts[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
