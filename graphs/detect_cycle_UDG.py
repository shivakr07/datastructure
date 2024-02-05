
def isCycle(self, V: int, adj: List[List[int]]) -> bool:
    #Code here
    def detect(adj, vis, src):
        q = []
        vis[src] = 1
        
        q.append([src, -1])
        
        while len(q):
            src = q[0][0]
            par = q[0][1]
            q.pop(0)
            
            for adjnode in adj[src]:
                if not(vis[adjnode]) :
                    vis[adjnode] = 1
                    q.append([adjnode, src])
                else:
                    if par != adjnode:
                        return True
        return False
    vis = [0 for i in range(V)]
    for i in range(len(vis)):
        if vis[i] != 1:
            if detect(adj, vis, i):
                return True
    return False