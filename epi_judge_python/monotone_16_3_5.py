
# Count number of monotone numbers of length k

# Runtime O(10*k) = O(k)
# Space O(10*k)
def count_monotone(k):
    counts = [[0] * k for _ in range(10)]

    for i in range(10):
        for j in range(k):
            if i == 0:
                counts[i][j] = 0
            elif j == 0:
                counts[i][j] = i 
            else:
                counts[i][j] = counts[i-1][j] + counts[i][j-1]

    return counts[-1][-1]

# For strictly monotone:
# counts[i][j] = counts[i-1][j-1] + counts[i-1][j]
# essentially can append new val to the end of all size-1 vals and without new val all of size
# ie. while going over row for digit 4, with say len = 3, 
# possible combinations are:
#        - append 4 to all values which use only 1-3 and len = 2
#        - all values which use only 1-3 and len = 3

for k in range(1, 10):
    print((k, count_monotone(k)))
