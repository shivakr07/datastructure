class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        arr1 = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(grid[i][j])
            arr1.append(temp)
        arr2 = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(grid[j][i])
            arr2.append(temp)
        print(arr1)
        print(arr2)
        count = 0
        for i in arr1:
            for j in arr2:
                if i == j:
                    count += 1
        return count

# took two tries to get submitted