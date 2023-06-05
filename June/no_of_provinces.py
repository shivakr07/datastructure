# number of provinces (using dfs)(connected components)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def buildgraph(isConnected):
            graph = {}
            # for i in range(len(isConnected)):
            for i in range(len(isConnected)):
                for j in range(len(isConnected)):
                    if isConnected[i][j] == 1:
                        if i in graph:
                            graph[i].append(j)
                        else:
                            graph[i] = [j]
            return graph
        
            
        def dfs_helper(vertex, visited):
            visited[vertex] = True
            # print(vertex, end=" ")

            for neighbour in graph[vertex]:
                if visited[neighbour] == False:
                    dfs_helper(neighbour, visited)

                
        visited = [False for i in range(len(isConnected))]
        graph = buildgraph(isConnected)
        def DFS(graph,nV, count):
            visited = [False for i in range(nV)]
            for src in graph:
                if visited[src] == False:
                    count += 1
                    dfs_helper(src, visited)
            return count

        return DFS(graph, len(graph),0)