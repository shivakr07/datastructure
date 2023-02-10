# conversion of the adjacency matrix into adjacency list

# a function which converts the adjmat graph into the adjlist
def adjlist(adjmat):
    graph = {}
    for i in range(len(adjmat)):
        for j in range(len(adjmat)):
            if adjmat[i][j] == 1:
                if i in graph:
                    graph[i].append(j)
                else:
                    graph[i] = [j]

    print(graph)
if __name__ == '__main__':
    # n, m = map(int, input.split())
    n = 5
    edges = [[0,1], [0,4], [1,2], [1,3], [1,4], [2,3], [3,4]]
    adjmat = [[0 for i in range(n)] for j in range(n)]
    # print(adjmat)
    for i in range(len(edges)):
        u, v = edges[i][0], edges[i][1]
        print(u, v)
        adjmat[u][v] = 1
        adjmat[v][u] = 1
    for i in adjmat:
        print(i)
    adjlist(adjmat)
        