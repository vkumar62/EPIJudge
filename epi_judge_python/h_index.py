from test_framework import generic_test
from collections import defaultdict

'''
   int[] s = new int[m.Length + 1];
    for (int i = 0; i < m.Length; i++) s[Math.Min(m.Length, m[i])]++;

    int sum = 0;
    for (int i = s.Length - 1; i >= 0; i--)
    {
        sum += s[i];
        if (sum >= i)
            return i;
    }

    return 0;
'''
# Variant - hindex in O(n) time
def h_index(citations):
    s = [0] * (len(citations)+1)
    for i in citations:
        s[min(len(citations), i)] += 1
   
    sums = 0
    for i in reversed(range(len(s))):
        sums += s[i]
        if (sums >= i):
            return i
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
