from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    intersections = []
    a_idx, b_idx = 0, 0
    
    while a_idx < len(A) and b_idx < len(B):
        if A[a_idx] == B[b_idx]:
            if not intersections or intersections[-1] != A[a_idx]:
                intersections.append(A[a_idx])
            a_idx, b_idx = a_idx + 1, b_idx + 1
        elif A[a_idx] < B[b_idx]:
            a_idx = a_idx + 1
        else:
            b_idx = b_idx + 1
    return intersections


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
