from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def detectcycle(self, src, adj, vis):
        vis[src] = True
        q = []
# 		vis = [False for i in range(V)]
		q.append([src, -1])
		
		while len(q) > 0:
		    node = q[0][0]
		    par = q[0][1]
		    q.pop(0)
		    for ad in adj[node]:
		        if vis[ad] == False:
		            vis[ad] = True
		            q.append([ad, node])
		        else:
		            if par != ad:
		                return True
        return False
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [False for i in range( V)]
		for i in range(0, V):
		    if vis[i] == False:
		        if self.detectcycle(i,adj,vis):
		            return True
		return False


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
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends