
# O(2^len(t)) time, O(len(t)) space in stack
def is_interleaving(s1, s2, s3):
    def is_interleaving_helper(s1, s1_idx, s2, s2_idx, s3, t_idx):
        if t_idx == len(s3):
            return True

        s1_match, s2_match = False, False
        if s1_idx < len(s1) and s3[t_idx] == s1[s1_idx]:
            s1_match = True
        if s2_idx < len(s2) and s3[t_idx] == s2[s2_idx]:
            s2_match = True

        if s1_match and s2_match:
            return any([is_interleaving_helper(s1, s1_idx+1, s2, s2_idx, s3, t_idx+1),
                    is_interleaving_helper(s1, s1_idx, s2, s2_idx+1, s3, t_idx+1)])
        elif s1_match:
            return is_interleaving_helper(s1, s1_idx+1, s2, s2_idx, s3, t_idx+1)
        elif s2_match:
            return is_interleaving_helper(s1, s1_idx, s2, s2_idx+1, s3, t_idx+1)
        else:
            return False

    if len(s1) + len(s2) != len(s3):
        return False
    return is_interleaving_helper(s1, 0, s2, 0, s3, 0)

s1 = 'gtaa'
s2 = 'atc'
t = 'gattaca'

#print(is_interleaving(s1, s2, t))

t = 'gatacta'
#print(is_interleaving(s1, s2, t))

t = 'gtataac'
#print(is_interleaving(s1, s2, t))

print(is_interleaving('aaa', 'aaa', 'aaaaaa'))

import pdb

class Solution:
    def isInterleave(self, s1, s2, s3):
#        pdb.set_trace()
        N = len(s1)
        M = len(s2)
        
        if N + M != len(s3):
            return False
        
        soln = [[False] * (M + 1) for _ in range(N + 1)]
        soln[0][0] = True
        
        for j in range(1, M+1):
            soln[0][j] = (s2[j-1] == s3[j-1] and soln[0][j-1])
            
        for i in range(1, N+1):
            soln[i][0] = (s1[i-1] == s3[i-1] and soln[i-1][0])
            
        for i in range(1, N+1):
#            pdb.set_trace() 
            s3_i = i - 1
            for j in range(1, M+1):
                soln[i][j] = any((soln[i-1][j] and s1[i-1] == s3[i-1+j], soln[i][j-1] and s2[j-1] == s3[i+j-1]))
        return soln[-1][-1]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().isInterleave(s1, s2, s3))
