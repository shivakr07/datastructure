class Solution:
    def minOperations(self, s: str) -> int:
        ar = []
        for i in range(len(s)):
            if i%2 == 0:
                ar.append('0')
            else:
                ar.append('1')
        ar2 = []
        for i in range(len(s)):
            if i%2 == 0:
                ar2.append('1')
            else:
                ar2.append('0')
        
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if s[i] != ar[i]:
                count1 += 1
        for i in range(len(s)):
            if s[i] != ar2[i]:
                count2 += 1
        print(count1,"", count2)
        return min(count1, count2)