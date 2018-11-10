import pdb


''' GeeksforGeeks
Input
2
6 6
5 0 5 2 2 3 3 1 4 0 4 1
13 8
0 1 0 2 0 3 0 6 0 7 1 3 1 4 2 4 2 5 3 4 4 6 4 7 5 6
'''

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
from collections import deque
from collections import defaultdict

def topo_sort(adj_matrix):
    # Using Kahn's algorithm

    #pdb.set_trace()
    V = len(adj_matrix)
    '''
    in_degree = [0] * V

    for j in range(V):
        in_degree[j] = sum(adj_matrix[i][j] for i in range(V))
    '''

    in_degree = list(sum(adj_matrix[i][j] for i in range(V)) for j in range(V))

    '''
    for i in range(V):
        for j in range(V):
            in_degree[j] += 1 if adj_matrix[i][j] else 0
    '''

    zero_degrees = deque((i for i,x in enumerate(in_degree) if x == 0))

    topo_order = []

    while len(zero_degrees):
        z = zero_degrees.popleft()

        for i in range(V):
            if adj_matrix[z][i]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    zero_degrees.append(i)
            adj_matrix[z][i] = 0

        topo_order.append(z)
    print(topo_order)
    return topo_order

from collections import deque
def topo_sort_dfs(adj_matrix):

    def dfs(i):
        if perm_mark[i]:
            return

        if temp_mark[i]:
            assert 0

        temp_mark[i] = True

        for j in range(V):
            if adj_matrix[i][j]:
                dfs(j)

        perm_mark[i] = True
        topo_sort.appendleft(i)

    V = len(adj_matrix)
    perm_mark = [False] * V
    temp_mark = [False] * V
    topo_sort = deque()

    for u in range(V):
        if not perm_mark[u]:
            dfs(u)
    ''' 
    while True:
        unvisited = None
        for i,x in enumerate(perm_mark):
            if not x:
                unvisited = i
        if unvisited:
            dfs(unvisited)
        else:
            break
    '''

    return list(topo_sort)


# GeeksforGeeks
# Graph(graph) is a defaultict of type List
# n is no of edges
def topoSort(n, graph):

    adj_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in graph[i]:
            adj_matrix[i][j] = 1

    return topo_sort_dfs(adj_matrix)

# Driver Program
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        # print res
        valid=True
        for i in range(N):
            n = len(graph[res[i]])
            for j in range(len(graph[res[i]])):
                for k in range(i+1, N):
                    if res[k]==graph[res[i]][j]:
                        n-=1
            # print n
            if n!=0:
                valid=False
                break
        if valid:
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

