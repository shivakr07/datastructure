# 0/1 matrix leetcode [diff is the only distance of 1 or 0 ]

from collections import deque
# if you will not use the deque then it will give time limit error
#Function to find distance of nearest 1 in the grid for each cell.
def nearest(self, grid):
    #Code here
    mat = grid
    n = len(mat)
    m = len(mat[0])
    q = deque()
    vis = [[0 for i in  range(m)] for i in range(n)]
    ans = [[0 for i in  range(m)] for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                q.append((i, j, 0))
                vis[i][j] = 1
            else:
                vis[i][j] = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while q:
        row, col, steps = q.popleft()

        ans[row][col] = steps
        
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            
            if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vis[nrow][ncol] == 0:
                q.append((nrow, ncol,steps+1))
                vis[nrow][ncol] = 1
            

    return ans 