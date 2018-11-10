import pdb

def merge_sort(A):
    def merge_sort_helper(A, l, r):
        if l == r:
            return

        mid = l + (r-l)//2

        merge_sort_helper(A, l, mid)
        merge_sort_helper(A, mid+1, r)
        merge(A, l, mid, r)

    def merge(A, left, middle, right):
        B = [0] * (right-left+1)
        l, r = left, middle+1

        for x in range(len(B)):
            if r > right: 
                B[x] = A[l]
                l += 1
            elif l > middle:
                B[x] = A[r]
                r += 1
            elif A[l] > A[r]:
                B[x] = A[r]
                r += 1
            else:
                B[x] = A[l]
                l += 1
        A[left:right+1] = B[:]
    
    merge_sort_helper(A, 0, len(A)-1)

def quick_sort(A):
    def quick_sort_helper(A, left, right):
        if right <= left:
            return

        #pdb.set_trace()

        pivot_index = right
        l = left

        for i in range(left, right):
            if A[i] < A[pivot_index]:
                A[l], A[i] = A[i], A[l]
                l += 1
        A[pivot_index], A[l] = A[l], A[pivot_index]
        #pdb.set_trace()
        quick_sort_helper(A, left, l-1)
        quick_sort_helper(A, l+1, right)

    quick_sort_helper(A, 0, len(A)-1)

    
import random
for _ in range(100):
    A = random.sample(range(10000), 100)
    B = A[:]
    merge_sort(A)
    assert sorted(B) == A, pdb.set_trace()

A = list(range(10, 0, -1))
merge_sort(A)
print(A)

print("QUICK SORT")
for _ in range(100):
    A = random.sample(range(10000), 100)
    B = A[:]
    quick_sort(A)
    assert sorted(B) == A, pdb.set_trace()

A = list(range(10, 0, -1))
quick_sort(A)
print(A)

