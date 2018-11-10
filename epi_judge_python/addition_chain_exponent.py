
# Not the right calculation
def addition_chain_exponent(n):
    ace = [0] * (n+1)
    ace[1] = 1

    for i in range(2, n+1):
        ace[i] = 1 + min((max(ace[x], ace[i-x]) for x in range(1, 1 + i//2)))

    print(list(enumerate(ace)))


from collections import deque
import pdb

class Node:
    def __init__(self, num=1, parents=None):
        self.depth = 0 
        self.num = num
        self.parents = set() if parents is None else parents
        self.children = set([num + num])
        self.children.update(set(num + x for x in self.parents))

    def __str__(self):
        return 'num: %s parents %s children %s' % (self.num, str(self.parents), str(self.children))
        
    def __repr__(self):
        return self.__str__()


def addition_chain_exponent(exps, N):
    q = deque([Node()])

    while q:
        node = q.popleft()

        exps[node.num] = min(exps[node.num], node.depth)

        for child in node.children:
            child_node = Node(child, set([node.num] + list(node.parents)))
            child_node.depth = node.depth + 1
            if child_node.num == N:
                exps[child_node.num] = min(exps[child_node.num], child_node.depth)
                child_node.parents.add(child_node.num)
                return child_node.parents
            q.append(child_node)

soln = [0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 6, 6, 7, 6, 7, 5, 6, 6, 7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 8, 6, 7, 7, 7, 7, 8, 7, 8, 7, 8, 8, 8, 7, 8, 8, 8, 6, 7, 7, 8, 7, 8, 8, 9, 7, 8, 8, 8, 8, 8, 8, 9, 7, 8, 8, 8, 8, 8, 8, 9, 8, 9, 8, 9, 8, 9, 9, 9, 7, 8, 8, 8, 8]

soln = [0] + soln[:]

exps = [float('inf')] * 1000*len(soln)
addition_chain_exponent(exps, len(soln) - 1)
addition_chain_exponent(exps, 101)
addition_chain_exponent(exps, 99)
addition_chain_exponent(exps, 98)
#print(exps)

for i in range(1, len(soln)):
    if exps[i] == float('inf'):
        print(i)
    else:
        assert exps[i] == soln[i], pdb.set_trace()



'''
for i, j in enumerate(soln):
    print(i, j)
    exp = addition_chain_exponent(i)
    assert exp == j, pdb.set_trace()
'''
#print(addition_chain_exponent(14))
#print(addition_chain_exponent(15))
#print(addition_chain_exponent(16))
