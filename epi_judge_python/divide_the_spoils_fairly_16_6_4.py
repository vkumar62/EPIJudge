
# Working solution at the end

def divide_spoils_fairly(spoils):
    
    def divide_helper(k, remaining):
        # Probably won't work. Needs a 2D array v[k][remaining]
        if k < 0:
            return 0

        if v[k] == -1:
            without_curr = divide_helper(k-1, remaining)
            with_curr = (0 if spoils[k] > remaining else (
                spoils[k] + divide_helper(k-1, remaining - spoils[k])))
            v[k] = max(without_curr, with_curr)
        return v[k]
    
    total = sum(spoils)
    v = [-1] * len(spoils)
    return divide_helper(len(spoils)-1, total//2)

# Return if any subset in A sums up to S
def subset_sum(A, S):
    def subset_sum_helper(i, remaining):
        # Does not work. Needs a 2D array s[i][remaining]
        if remaining == 0:
            return True

        if i < 0:
            return False

        if s[i] is None:
            without_curr = subset_sum_helper(i-1, remaining)
            with_curr = (False if remaining < A[i] else (
                subset_sum_helper(i-1, remaining - A[i])))
            s[i] = any([without_curr, with_curr])
        return s[i]

    def subset_sum_helper_recurse(i, remaining):
        if remaining == 0:
            return True

        if i < 0:
            return False

        without_curr = subset_sum_helper_recurse(i-1, remaining)
        with_curr = (False if remaining < A[i] else (subset_sum_helper_recurse(i-1, remaining - A[i])))
        return any([without_curr, with_curr])

    s = [None] * len(A)
    #return subset_sum_helper_recurse(len(A)-1, S)
    return subset_sum_helper(len(A)-1, S)


A = [4,1,10,12,5,2]
S = 9

#print(subset_sum(A,S))

A = [1,8,2,5]
S = 4 

#print(subset_sum(A,S))

class Spoils:
    def __init__(self):
        self.total = 0
        self.items = []

    def __str__(self):
        return 'total %s items %s' % (self.total, str(self.items))

    def __repr__(self):
        return self.__str__()

import pdb
def divide_spoils_fairly(A):
    # Store the loots for thief A such that it sums upto sum(A)//2
    # Follows the 0/1 knapsack algorithm
    lootA = [[Spoils() for _ in range(1 + sum(A)//2) ] for _ in range(1+len(A))]
    #pdb.set_trace()

    for i in range(1, len(lootA)):
        for j in range(1, len(lootA[0])):
            if j >= A[i-1] and ((lootA[i-1][j-A[i-1]].total + A[i-1]) > lootA[i-1][j].total):
                lootA[i][j].total = lootA[i-1][j-A[i-1]].total + A[i-1]
                lootA[i][j].items = lootA[i-1][j-A[i-1]].items + [A[i-1]]
            else:
                lootA[i][j].total = lootA[i-1][j].total
                lootA[i][j].items = lootA[i-1][j].items

    print(lootA[-1][-1])
    return lootA[-1][-1].items

A = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
B = divide_spoils_fairly(A)
print(B)
print(sum(B))
