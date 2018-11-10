from test_framework import generic_test
import pdb


def levenshtein_distance(A, B):
    # TODO - you fill in here.
    min_, max_ = sorted((A,B))
#    if len(A) < len(B):
#        min_, max_ = A, B
#    else:
#        min_, max_ = B, A

#    pdb.set_trace()
    dists = [x for x in range(len(min_) + 1)]

    for x in range(1, len(max_) + 1):
        dists[0] = x
        prev_diag_val = x-1
        for y in range(1, len(min_) + 1):
            diag_val = dists[y]
            if min_[y-1] == max_[x-1]:
                dists[y] = prev_diag_val
            else:
                dists[y] = 1 + min(prev_diag_val, 
                                  dists[y],
                                  dists[y-1])
            prev_diag_val = diag_val
        #print(dists)

    return dists[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
