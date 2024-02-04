def bfs(adj, V, i, j, vis):
    q = []
    q.append([i, j])
    vis[i][j] = True
    while len(q):
        row, col = q[0][0], q[0][1]
        q.pop(0)
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                nrow = row + i
                ncol = col + j
                if nrow > 0 and nrow <= V and  ncol > 0 and ncol <= V:
                    if vis[nrow][ncol] == False:
                        q.append([nrow, ncol])
                        vis[nrow][ncol] = True
def numProvinces(adj, V):
    vis = [ [False for i in range(V+1)] for j in range(V+1)] 
    count = 0
    for i in range(V+1):
        for j in range(V+1):
            if adj[i][j] == True and vis[i][j] == False:
                count += 1
                bfs(adj, V, i, j, vis)
    return count
