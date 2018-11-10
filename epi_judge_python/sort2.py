def merge_sort(A):
    def merge_helper(A, left, right, B):
        if left >= right:
            return

        mid = (left + right)//2
        merge_helper(A, left, mid, B)
        merge_helper(A, mid+1, right, B)
        merge(A, left, mid, right, B)

    def merge(A, left, mid, right, B):
        l, r = left, mid+1
        B[left:right+1] = A[left:right+1]

        for i in range(left, right+1):
            if l > mid:
                A[i] = B[r]
                r += 1
            elif r > right:
                A[i] = B[l]
                l += 1
            elif B[l] > B[r]:
                A[i] = B[r]
                r += 1
            else:
                A[i] = B[l]
                l += 1
    merge_helper(A, 0, len(A)-1, [0]*len(A))


def quick_sort(A):
    def quick_sort_helper(A, left, right):
        if right <= left:
            return

        pivot = A[right]
        pivot_index = left

        for i in range(left, right):
            if A[i] < pivot:
                A[pivot_index], A[i] = A[i], A[pivot_index]
                pivot_index += 1

        A[pivot_index], A[right] = A[right], A[pivot_index]
        quick_sort_helper(A, left, pivot_index-1)
        quick_sort_helper(A, pivot_index+1, right)

    quick_sort_helper(A, 0, len(A)-1)



import random
import pdb
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

