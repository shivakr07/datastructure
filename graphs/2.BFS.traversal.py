# bfs graph traversal / level order traversal
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

def BFS(graph, src):
    visited = [False for i in range(4)] 
    queue = []
    # print(visited)
    queue.append(src)
    visited[src] = True
    
    while len(queue):
        popped_item = queue.pop(0)
        print(popped_item)
        
        for i in graph[popped_item]:
            if visited[i] == False:
                queue.append(i)
                # print(i)
                visited[i] = True 

if __name__ == '__main__':
    n = 4
    edges = [[0,1], [0,2], [1,2], [2,0], [2,3], [3,3]]
    graph = build_graph(edges, n)
    BFS(graph, 2)
    
'''
# bfs of the gfg

#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited = [0 for i in range(V)]
        # print(V)
        ans = []
        
        visited[0] = 1
        queue = [0]
        # node = queue[0]
        while len(queue):
            node = queue.pop(0)
            ans.append(node)
            
            for item in adj[node]:
                if visited[item] == 0:
                    queue.append(item)
                    visited[item] = 1
        return ans
        

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
'''