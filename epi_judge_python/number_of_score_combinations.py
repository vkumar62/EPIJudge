from test_framework import generic_test


# Time - O(final_score * play_scores)
# Space - O(final_score)
def num_combinations_for_final_score(final_score, individual_play_scores):
    num_combs = [0] * (final_score+1)
    num_combs[0] = 1

    for play in individual_play_scores:
        for score in range(play, final_score+1):
            num_combs[score] += num_combs[score-play]
    
    return num_combs[-1]

#Variants
def count_all_comb(N, valids):
    c = [0] * (N+1)
    c[0] = 1
    # For each score, figure out the number of combinations possible
    for i in range(N+1):
        # If score x can be performed in A combinations, score (x + v) 
        # can be done in A combinations for each v by appending
        for v in valids:
            if i >= v:
                c[i] += c[i-v]
    print(c)
    return c[-1]

def get_all_comb(N, valids):
    c = [0] * (N+1)
    c[0] = 1
    combs = [[] for _ in range(N+1)]
    combs[0].append([])
    for i in range(N+1):
        for v in valids:
            if i >= v:
                c[i] += c[i-v]
#                pdb.set_trace()
                for prev_comb in combs[i-v]:
                    combs[i].append(copy.deepcopy(prev_comb + [v]))
#                combs[i].extend(copy.deepcopy(combs[i-v]))
#                for x in combs[i]:
#                    x.append(v)
    for i in range(N+1):
        assert len(combs[i]) == c[i]
    print(combs)
    return combs[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
