class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        q = collections.deque()
        for x in range(row):
            for y in range(col):
                if matrix[x][y] == 0:
                    q.append((x, y))
                else:
                    matrix[x][y] = float('inf')
        
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and matrix[new_x][new_y] > matrix[x][y] + 1:
                    q.append((new_x, new_y))
                    matrix[new_x][new_y] = matrix[x][y] + 1
        
        return matrix