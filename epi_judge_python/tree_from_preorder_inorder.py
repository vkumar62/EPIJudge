from test_framework import generic_test

from binary_tree_node import BinaryTreeNode

import pdb

def binary_tree_from_preorder_inorder(preorder, inorder):
    def create_subtree(pre_start, pre_end, in_start):
        #pdb.set_trace()
        #if pre_end <= pre_start or in_end <= in_start:
        if pre_end <= pre_start:
            return None

        root_index = inorder.index(preorder[pre_start])
        left_subtree_size = root_index - in_start

        return BinaryTreeNode(preorder[pre_start], 
                create_subtree(pre_start + 1, pre_start + 1 + left_subtree_size,
                               in_start),
                create_subtree(pre_start + 1 + left_subtree_size, pre_end,
                               root_index + 1))

    return create_subtree(0, len(preorder), 0)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
