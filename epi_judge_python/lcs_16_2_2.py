#code
import sys

def LCS(A, B):
    lcs = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    
    s = ''
    i = len(A)
    j = len(B)

    print(lcs)

    while i != 0 and j != 0:
        if A[i-1] == B[j-1]:
            s = A[i-1] + s
            i -= 1
            j -= 1
        elif lcs[i-1][j] < lcs[i][j-1]:
            j -= 1
        else:
            i -= 1

    return lcs[-1][-1], s

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])
    for n, A, B in zip(*[iter(lines[1:])]*3):
        #print(A)
        #print(B)
        print(LCS(A.rstrip(),B.rstrip()))

def test():
    A = 'carthorse'
    B = 'orchestra'

    print(LCS(A,B))
