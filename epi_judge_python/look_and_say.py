from test_framework import generic_test

import pdb

def look_and_say(n):
    # TODO - you fill in here.
    def next_num(x):
#        pdb.set_trace()
        s = []
        c = 1 

        for i in range(1, len(x)):
            if x[i] != x[i-1]:
                s.append(c)
                s.append(x[i-1])
                c = 1 
            else:
                c += 1

        s.append(c)
        s.append(x[-1])
        return s

    res = [1]
    for i in range(1, n):
        res = next_num(res)

    return ''.join(map(str, res))





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
