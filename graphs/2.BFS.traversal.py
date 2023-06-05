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






# -------------------------------------------

x,y,p,q = map(int, input().split())
if y % x == 0:
    print(-1)
else:
    target = y // x
    def count(x, y,p, q, co):
        if y == x:
            return count
        if y < x:
            return -1
        
        return count(x*p, y, p, q, co+1)
    print(count(x,y,p,q,0))
    
# -----------------------------------------------


# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP


def knapsack(wt, val, W, n):

	# base conditions
	if n == 0 or W == 0:
		return 0
	if t[n][W] != -1:
		return t[n][W]

	if wt[n-1] <= W:
		t[n][W] = max(
			val[n-1] + knapsack(wt, val, W-wt[n-1], n-1),
			knapsack(wt, val, W, n-1))
		return t[n][W]
	elif wt[n-1] > W:
		t[n][W] = knapsack(wt, val, W, n-1)
		return t[n][W]

# Driver code
if __name__ == '__main__':
	profit = [60, 100, 120]
	weight = [10, 20, 30]
	W = 50
	n = len(profit)
	
	t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
	print(knapsack(weight, profit, W, n))



def knapsack(wt, val, W, n):
    dp = [[0 for i in range(W+1)] for j in range(n+1)] 
    # create dp table
    
    # initialization of DP table
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    # fill remaining cell of DP
    for i in range(n+1):
        for j in range(W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

                