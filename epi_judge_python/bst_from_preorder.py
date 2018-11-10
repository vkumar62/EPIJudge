from test_framework import generic_test
import pdb

class BinaryTreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def rebuild_bst_from_preorder(preorder_sequence):
    # TODO - you fill in here.
    def build_bst_helper(pre_start, pre_end):

#        pdb.set_trace()
        if pre_end < pre_start:
            return None

        root_data = preorder_sequence[pre_start]
    
        right_start = pre_start+1
        while right_start <= pre_end and preorder_sequence[right_start] <= root_data:
            right_start += 1

        return BinaryTreeNode(preorder_sequence[pre_start],
                       build_bst_helper(pre_start + 1, right_start-1),
                       build_bst_helper(right_start, pre_end))

    return build_bst_helper(0, len(preorder_sequence)-1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
