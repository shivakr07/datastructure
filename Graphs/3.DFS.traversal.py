# defpth search traversal 

def build_graph(edges, n):
    graph = {}
    
    for i in range(n):
        graph[i] = []
        
    for edge in edges:
        src =  edge[0]
        dest = edge[1]
        
        graph[src].append(dest)
        graph[dest].append(src)

    return graph

# dfs_helper() for traversing all the neighbours of the vertex
def dfs_helper(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")
    
    for neighbour in graph[vertex]:
        if visited[neighbour] == False:
            dfs_helper(neighbour, visited)
    
# dfs function
def DFS(graph, src, nV):
    visited = [False for i in range(nV)]
    dfs_helper(src, visited)
            

if __name__ == '__main__':
    n = 4
    edges = [[0,1], [0,2], [1,2], [2,0], [2,3], [3,3]]
    graph = build_graph(edges, n)
    DFS(graph, 2, n)
