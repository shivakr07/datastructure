class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def recurs(grid,row, col,  n, m):
            grid[row][col] = '$'
            
            if row-1 >= 0 and grid[row-1][col] == '1':
                recurs(grid,row-1, col, n, m )
            if row+1 < n and grid[row+1][col] == '1':
                recurs(grid,row+1, col, n, m )
            if col-1 >= 0 and grid[row][col-1] == '1':
                recurs(grid,row, col-1, n, m )
            if col+1 < m and grid[row][col+1] == '1':
                recurs(grid,row, col+1, n, m )
                    
                    
                    
                    
        
        def dfs(grid):
            n = len(grid)
            m = len(grid[0])
            count = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == '1':
                        count += 1
                        recurs(grid,i, j,  n, m)
                        
            return count
        return dfs(grid)
        