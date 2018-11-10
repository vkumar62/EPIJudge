from test_framework import generic_test

from collections import deque

def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if not tree:
        return []

    this_level = deque([tree])
    results = []

    while this_level:
        this_level_nodes = [] 
        next_level = deque()
        while this_level:
            node = this_level.popleft()
            this_level_nodes.append(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        results.append(this_level_nodes)
        this_level = next_level

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
