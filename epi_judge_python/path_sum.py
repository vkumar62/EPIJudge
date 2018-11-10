from test_framework import generic_test

import pdb

def has_path_sum(tree, remaining_weight):
    def has_path_sum_helper(tree, remaining_weight):
        #pdb.set_trace()
        if tree is None:
            return False 

        if tree.right is None and tree.left is None:
            return remaining_weight == tree.data

        return (has_path_sum_helper(tree.right, remaining_weight-tree.data) or
                has_path_sum_helper(tree.left, remaining_weight-tree.data))

    return has_path_sum_helper(tree, remaining_weight)

def path_sum_paths(tree, remaining_weight):
    def path_sum_helper(tree, remaining_weight, path):
        #pdb.set_trace()
        if tree is None:
            return False 

        path.append(tree.data)
        if tree.right is None and tree.left is None:
            if remaining_weight == tree.data:
                paths.append(path[:])

        ret = path_sum_helper(tree.right, remaining_weight-tree.data, path) or \
                path_sum_helper(tree.left, remaining_weight-tree.data, path)
        path.pop()
        return ret
    paths = []
    path_sum_helper(tree, remaining_weight, [])
    print(remaining_weight, paths)
    for path in paths:
        assert sum(path) == remaining_weight
    return has_path_sum(tree, remaining_weight)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       path_sum_paths))
