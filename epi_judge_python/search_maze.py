import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import pdb

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
def get_all_neighbors(maze, cur):
    neighbors = []
    x,y = cur

    if x-1 >= 0 and maze[x-1][y] == WHITE:
        neighbors.append(Coordinate(x-1, y))
    if x+1 < len(maze) and maze[x+1][y] == WHITE:
        neighbors.append(Coordinate(x+1, y))

    if y-1 >= 0 and maze[x][y-1] == WHITE:
        neighbors.append(Coordinate(x, y-1))
    if y+1 < len(maze[0]) and maze[x][y+1] == WHITE:
        neighbors.append(Coordinate(x, y+1))

#    for xo in range(-1, 2):
#        for yo in range(-1, 2):
#            xi = x+xo
#            yi = y+yo
#            if xi < 0 or xi >= len(maze):
#                continue
#            if yi < 0 or yi >= len(maze[0]):
#                continue
#            if maze[xi][yi] == 0:
#                neighbors.append(Coordinate(xi, yi))
    return neighbors

def solve_maze_dfs_helper(maze, cur, e, path):
    if (cur == e):
        path.append(cur)
        return True

    x,y = cur
    if maze[x][y] == 1:
        return False

    maze[x][y] = 1
    path.append(cur)

    for neighbor in get_all_neighbors(maze, cur):
        solved = solve_maze_helper(maze, neighbor, e, path)
        if solved:
            return True
    del path[-1]
    return False

def search_maze_dfs(maze, s, e):
    # TODO - you fill in here.
    path = []
    solved = solve_maze_dfs_helper(maze, s, e, path)
#    pdb.set_trace()
    return path

def search_maze_bfs(maze, s, e):
    q = [s]
    path = []
    prev = {}

    while len(q):
        cur = q.pop(0)

        if cur == e:
            break

        for neighbor in get_all_neighbors(maze, cur):
            if neighbor not in prev:
                q.append(neighbor)
                prev[neighbor] = cur

    dest = e
    if dest:
        while dest != s:
            path.append(dest)
            dest = prev[dest]
        path.append(dest)
    return path.reverse()

def search_maze(maze, s, e):
    # TODO - you fill in here.
    return search_maze_bfs(maze, s, e)

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
