''' GeeksforGeeks

Input
2
2
0 25 25 0
0
3
0 1 43 1 0 6 43 6 0
2

Output
0 25
7 6 0

1
4
0 23 19 33 23 0 18 31 19 18 0 13 33 31 13 0
3

'''

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# The function prints V space separated integers where 
# the ith integer denote the shortest distance of ith vertex
# from source vertex

def min_vertex(v, dist, unvisited):
    mind = sys.maxsize
    minv = None

    for u in unvisited:
        if dist[u] < mind:
            mind = dist[u]
            minv = u
    return minv


import sys
def dijkstra(graph, v, s):
    # Code here
    unvisited = set(range(v))
    dist = [sys.maxsize] * v 
    #prev = [None] * v

    dist[s] = 0
    
    while len(unvisited):

        u = min_vertex(v, dist, unvisited)
        #u = dist.index(min((dist[x] for x in unvisited)))
        unvisited.remove(u)

        for j in range(v):
            if graph[u][j]:
                new_dist = dist[u] + graph[u][j]
                if new_dist < dist[j]:
                    dist[j] = new_dist
                    #prev[j] = u

    #print(' '.join(map(str, dist)))
    print(*dist, sep=' ')


# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[c]
                c+=1
        s = int(input())
        dijkstra(matrix, n, s)
        print('')
# Contributed By: Harshit Sidhwa

