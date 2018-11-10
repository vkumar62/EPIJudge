

'''
   GGGGBBBB???????YYYYRRRR

   When doing ?, if it is G, swap with the first B 
   if it is B, just continue
   if it is Y, swap with the first left side ?
   if it is R, do a chain swap
'''
VALS = ['G', 'B', 'Y', 'R']
def dutch_national_4_colors(A):
    left = mid1 = 0
    mid2 = right = len(A)-1

    while mid1 <= mid2:
        if A[mid1] == VALS[0]:
            A[left], A[mid1] = A[mid1], A[left]
            left, mid1 = left + 1, mid1 + 1
        elif A[mid1] == VALS[1]:
            mid1 += 1
        elif A[mid1] == VALS[2]:
            A[mid2], A[mid1] = A[mid1], A[mid2]
            mid2 -= 1
        else:
            A[right], A[mid2], A[mid1] = A[mid1], A[right], A[mid2]
            mid2 -= 1
            right -= 1


A = list('GBYRRRRRGGGGYYYRRRBBBB')
print(A)
dutch_national_4_colors(A)
print(A)
