class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        summ = 0
        altitude = [0]
        for i in gain:
            summ += i
            altitude.append(summ)
        return max(altitude)