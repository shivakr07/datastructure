#done with the rotting oranges 
# it is necessary to identify thr dfs vs bfs 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfs(grid):
            n = len(grid)
            m = len(grid[0])
            q = []
            visited = [[0 for i in range(m)] for j in range(n)]
            
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 2:
                        q.append([(i, j), 0])
                        visited[i][j] = 2
                    else:
                        visited[i][j] = 0
            
            totmins = 0
            delrow = [-1, 0, 1, 0]
            delcol = [0, 1, 0, -1]
            
            while len(q):
                row = q[0][0][0]
                col = q[0][0][1]
                t = q[0][1]
                totmins = max(totmins, t)
                q.pop(0)
                
                for i in range(4):
                    nrow = row + delrow[i]
                    ncol = col + delcol[i]
                    
                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                        q.append([(nrow, ncol), t+1])
                        visited[nrow][ncol] = 2
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and visited[i][j] != 2:
                        return -1
            return totmins
        
        return bfs(grid)
                    
                    
                    
                    
                    
                    
                    