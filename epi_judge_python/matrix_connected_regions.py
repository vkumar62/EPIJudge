from test_framework import generic_test
from collections import deque

import pdb

def flip_color_dfs(x, y, image):
    def dfs_helper(i, j):
        if i< 0 or i >= len(image) or j < 0 or j >= len(image[0]):
            return

        if image[i][j] != orig_color:
            return

        image[i][j] = 1 - orig_color 
        for a, b in zip([i-1, i, i, i+1], [j, j-1, j+1, j]):
            dfs_helper(a,b)

#    pdb.set_trace()
    orig_color = image[x][y]
    dfs_helper(x, y)

def flip_color_bfs(x, y, image):
    q = deque()
    q.append((x,y))
    color = image[x][y]
    while q:
        i,j = q.popleft()
        image[i][j] = 1 - color
        for a, b in zip([i-1, i, i, i+1], [j, j-1, j+1, j]):
            if a >= 0 and a < len(image) and b >= 0 and b < len(image[0]) and image[a][b] == color:
                q.append((a,b))

    
        

def flip_color(x, y, image):
    # TODO - you fill in here.
    flip_color_bfs(x, y, image)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
