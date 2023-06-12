#  it seems easy but it was a good question

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ans = []
        
        i = 0
        while i < len(nums):
            st = nums[i]
            while i < len(nums)-1 and nums[i+1] == nums[i] + 1:
                i += 1
            end = nums[i]
            
            if st == end:
                ans.append(str(st))
            else:
                ans.append(str(st) + "->" + str(end))
            
            i += 1
        return ans