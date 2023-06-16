class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dir = [(1,0), (0,1), (-1,0), (0,-1)]
        n = len(grid)
        m = len(grid[0])
        vis = [[False for i in range(m)] for j in range(n)]
        def bfs(row, col):
            q = []
            q.append([(row, col), (-1,-1)])
            value = grid[row][col]
            vis[row][col] = True
            
            while len(q) > 0:
                curr = q[0][0]
                prev = q[0][1]
                q.pop(0)
                for dr,dc in dir:
                    nrow = curr[0] + dr
                    ncol = curr[1] + dc
                    
                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == value and (nrow, ncol) != prev:
                        if vis[nrow][ncol]:
                            return True
                        q.append([(nrow,ncol),curr])
                        vis[nrow][ncol] = True
            return False
        
        for i in range(n):
            for j in range(m):
                if vis[i][j] == False:
                    if bfs(i, j):
                        return True
        return False

#  my logic was same but little mistakes here and there