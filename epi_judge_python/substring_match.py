from test_framework import generic_test


def rabin_karp(t, s):
    # TODO - you fill in here.
    BASE = 26
    power = 1
    s_hash = 0

    for c in s:
        s_hash = (s_hash * BASE) + ord(c)-ord('a')
        power *= BASE

    #power = BASE**(len(s)-1)
    power //= BASE

    t_hash = 0
    for i, c in enumerate(t):
        if t_hash == s_hash and t[i-len(s):i] == s:
            return i-len(s)
        # update t_hash
        
        if i >= len(s):
            t_hash -= power * (ord(t[i-len(s)]) - ord('a'))
        t_hash = (t_hash * BASE) + ord(c)-ord('a')

    if t_hash == s_hash and t[len(t)-len(s):len(t)] == s:
        return len(t)-len(s)
    return -1 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
