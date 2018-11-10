

# Also in Leetcode 654  https://leetcode.com/problems/maximum-binary-tree/description/

class TreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

#Time O(n^2)
# O(n) time is probably Cartesian tree see wikipedia https://en.wikipedia.org/wiki/Cartesian_tree
def max_tree(A):
    def max_tree_helper(start, end):
        if end <= start:
            return None

        # root is the index of the highest entry in this subarray
        max_val = A[start] 
        maxi = start
        for i in range(start+1, end):
            if max_val < A[i]:
                max_val = A[i]
                maxi = i

        root_index = maxi
        return TreeNode(max_val, 
                max_tree_helper(start, maxi),
                max_tree_helper(maxi, end))

    return max_tree_helper(0, len(A))


