# number of connected components in matrix or number of islands

class Solution:
    def numIslands(self, grid):
        def dfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1) 
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def recurs(grid, visited, i, j):
            if i-1 >= 0 and i+1 < len(grid[0]) and j-1 >= 0 and j+1 < 0:
                if grid[i-1][j] == grid[i][j]:
                    visited[i-1][j] = True
                if grid[i+1][j] == grid[i][j]:
                    visited[i+1][j] = True
                if grid[i][j-1] == grid[i][j]:
                    visited[i][j-1] = True
                if grid[i][j+1] == grid[i][j]:
                    visited[i][j+1] = True
                    
        def dfs(grid):
            count = 0
            visited = [False for i in range(len(grid[0]) for j in range(len(grid)))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if visited[grid[i][j]] == False:
                        count += 1
                        recurs(grid, i, j)
            return count
        return dfs(grid)