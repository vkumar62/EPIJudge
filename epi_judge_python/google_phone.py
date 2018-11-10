'''You are given a square grid of size dxd. It contains each of the numbers 1..n, where n = d^2. The numbers each occur once and only once, in arbitrary order, find the length of the longest sequence of adjacent consecutive numbers in the grid. 


For example, 


1 2 9 

5 3 8 

4 6 7 


This contains three sequences of adjacent numbers [1, 2, 3], [4, 5], and [6, 7, 8, 9]. The longest is [6, 7, 8, 9], which has length 4, and therefore the answer is 4.
'''



def longest_consecutive(grid):
    # grid - list[list[int]]
    def get_neighbors(i,j):
         neighbors = [(x,y) for x,y in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)) if 0 <= x < N and 0 <= y < N]
         return neighbors

    def dfs_helper(i, j, visited, depth):
         if visited[i][j]:
             return 0
         visited[i][j] = True
         neighbors = get_neighbors(i, j)
         for x,y in neighbors:
              if grid[x][y] == grid[i][j] + 1:
                     length = dfs_helper(x, y, visited, depth+1)
                     return length
         return depth

    #Time - O(N^2 * Longest consecutive) = O(N^4)
    # Space - stack depth - O(longest consecutive) = O(N^2)
    if not grid:
        return 0
    N = len(grid)
    max_len = 0
    for i in range(N):
         for j in range(N):
            visited = [[False] * N for _ in range(N)]
            length = dfs_helper(i, j, visited, 1)
            max_len = max(max_len, length)
    return max_len

import pdb
def longest_consecutive(grid):

    # Time - O(N^2)
    # Space - O(N^2)
    def is_neighbor(x1, y1, x2, y2):
        if abs(x2-x1) == 1 and y1 == y2:
            return True
        if abs(y2-y1) == 1 and x2 == x1:
            return True
        return False

    pdb.set_trace()
    N = len(grid)
    positions = [None] * (N*N)

    for i in range(N):
        for j in range(N):
            positions[grid[i][j]-1] = (i, j)

    max_len = 0
    cur_len = 1
    for i in range(1, N*N):
        if is_neighbor(*positions[i], *positions[i-1]):
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1

    return max_len
 

grid = [[1, 2, 9], [5, 3, 8], [4, 6, 7]]
print(longest_consecutive(grid))

