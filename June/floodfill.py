class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        q = []
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        
        for i in range(len(image)):
            for j in range(len(image[0])):
                if i == sr and j == sc:
                    q.append([i, j])
        tempcol = image[sr][sc]
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        while len(q) > 0:
            row = q[0][0]
            col = q[0][1]
            q.pop(0)
            image[row][col] = color
            visited[row][col] = True
            for i in range(4):
                newrow = row + delrow[i]
                newcol = col + delcol[i]
                
                if newrow >= 0 and newrow < len(image) and newcol >= 0 and newcol < len(image[0]) and visited[newrow][newcol] == False  and image[newrow][newcol] == tempcol:
                    q.append([newrow, newcol])
        return image

# till now we have done it using bfs