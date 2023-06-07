class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxm = 0
        count = 0
        for i in range(len(nums)):
            if 1 & nums[i] == 1:
                count += 1
                if count > maxm:
                    maxm = count
            else:
                count = 0
        return maxm