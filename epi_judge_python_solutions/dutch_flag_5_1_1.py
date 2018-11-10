def dutch_flag_1(A):
    val1, val2, val3 = 0, 0, len(A)

    while val2 < val3:
        if A[val2] == VAL1:
            A[val1], A[val2] = A[val2], A[val1]
            val1, val2 = val1 + 1, val2 + 1
        elif A[val2] == VAL2:
            val2 += 1
        else:
            val3 -= 1
            A[val3], A[val2] = A[val2], A[val3]
