from lcs_16_2_2 import *
import sys
import pdb

# Compute min number of characters to delete from A to make it a palindrome
#2 methods
# - Compute the LCS of A and reverse of A. Subtract from len(A)
# - OR
#    if A[l] == A[r]:
#          c[l][r] = c[l+1][r-1]
#    else:
#          c[l][r] = min(c[l+1][r], c[l][r-1])
def min_remove_lcs(A):
    #pdb.set_trace()
    lcs, _ = LCS(A, A[::-1])
    return len(A) - lcs

def min_remove_dp(A):

    def min_remove_dp_helper(A, l, r, c):
        #pdb.set_trace()
        if l > r:
            c[l][r] = 10000
        if l == r:
            c[l][r] = 0 
        if l == r-1:
            if A[l] == A[r]:
                c[l][r] = 0
            else:
                c[l][r] = 1

        if c[l][r] is None:
            if A[l] == A[r]:
                  c[l][r] = min_remove_dp_helper(A, l+1, r-1, c)
            else:
                  c[l][r] = 1 + min(min_remove_dp_helper(A, l+1, r, c), min_remove_dp_helper(A, l, r-1, c))
        return c[l][r]
    c = [[None] * len(A) for _ in range(len(A))]
    min_remove_dp_helper(A, 0, len(A)-1, c)
    print(c)
    return c[0][-1]

#    def min_remove_dp_helper(A, l, r ):
#        #pdb.set_trace()
#        if l > r:
#            return 10000
#        if l == r:
#            return 0 
#        if l == r-1:
#            if A[l] == A[r]:
#                return 0
#            else:
#                return 1
#
#        if A[l] == A[r]:
#              return min_remove_dp_helper(A, l+1, r-1)
#        else:
#              return 1 + min(min_remove_dp_helper(A, l+1, r), min_remove_dp_helper(A, l, r-1))
#
#    x = min_remove_dp_helper(A, 0, len(A)-1)
#    print(x)
#    return x
#

print(min_remove_dp('geeks'))
