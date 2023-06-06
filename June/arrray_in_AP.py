# < check if array can be converted in ap or not>
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) != d:
                return False
        return True
            
            