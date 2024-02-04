class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        q = []
        vis = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([[i, j], 0])
                    vis[i][j] = 2
                else:
                    vis[i][j] = 0
        tm = 0
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        while q:
            r = q[0][0][0]
            c = q[0][0][1]
            t = q[0][1]
            
            tm = max(tm, t)
            q.pop(0)
            for i in range(4):
                nrow = r + dr[i]
                ncol = c + dc[i]
                
                if nrow >= 0 and nrow < m and ncol >=0 and ncol < n and vis[nrow][ncol] ==0 and grid[nrow][ncol] == 1:
                    q.append([nrow, ncol], t+1)
                    vis[nrow][ncol] = 2
        for i in range(m):
            for j in range(n):
                if vis[i][j] != 2 and grid[i][j] == 1:
                    return -1
        return tm