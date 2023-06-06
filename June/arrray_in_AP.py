# < check if array can be converted in ap or not>
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) != d:
                return False
        return True
            
# < arithmetic subarrays >
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        #function to check an array is ap 
        def isAp(arr):
            if len(arr) <= 1:
                return True
            arr.sort()
            d = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if (arr[i] - arr[i-1])  != d:
                    return False
            return True
        
        ans = []
        for i in range(len(l)):
            left, right = l[i], r[i]+1
            temp = nums[left:right]
            if isAp(temp):
                ans.append(True)
            else:
                ans.append(False)
        return ans
                    
            
