# sanket singh lecture 1  :

# <1> DFS  
# <connected components><visited nodes><permutation swaps>

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def buildgraph(isConnected):
            graph = {}
            for i in range(len(isConnected))
            for i in range(len(isConnected)):
                for j in range(len(isConnected[0])):
                    if isConnected[i][j] == 1:
                        graph[i].append(j)
                        graph[j].append(i)
            count = 0
            def dfs_helper(vertex, visited):
                visited[vertex] = True
            # print(vertex, end=" ")

                for neighbour in graph[vertex]:
                    if visited[neighbour] == False:
                        dfs_helper(neighbour, visited)
                
            visited = [False for i in range(len(isConnected))]
            
            def DFS(graph,nV, count):
                visited = [False for i in range(nV)]
                for src in graph:
                    if visited[src] == False:
                        count += 1
                        dfs_helper(src, visited)
                return count
            
            return DFS(graph, len(graph),0)