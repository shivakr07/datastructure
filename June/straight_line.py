class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0),(x1, y1) = coordinates[0], coordinates[1]
        
        for i in range(2, len(coordinates)):
            x,y = coordinates[i]
            if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
                return False
        return True
