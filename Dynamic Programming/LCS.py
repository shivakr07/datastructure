#  longest common subsequence

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        def LCS(s1, s2, i, j, dp):
            if i <= 0 or j <= 0:
                return 0
            
            if dp[i-1][j-1] != -1:
                return dp[i-1][j-1]
            
            if s1[i-1] == s2[j-1]:
                dp[i-1][j-1] = 1 + LCS(s1, s2, i-1, j-1, dp)
                return dp[i-1][j-1]
            else:
                dp[i-1][j-1] = max(LCS(s1, s2, i-1, j, dp), LCS(s1, s2, i, j-1, dp))
                return dp[i-1][j-1]
        dp = [[-1 for i in range(len(s2))] for j in range(len(s1))]   
        return LCS(s1, s2, len(s1), len(s2), dp)
        
def fun(i, j, dp):
    # Write your code here
        if i < 0 or j < 0:
            return 0 
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] =  1 + fun(i-1, j-1, dp)
            return dp[i][j]
        else:
            dp[i][j] = max(fun(i-1,j, dp), fun(i, j-1, dp))
            return dp[i][j]
s1, s2 = '', ''
n = len(s1)
m = len(s2)
dp = [[-1 for i in range(m)] for j in range(n)]
# return fun(n-1, m-1, dp)
dp = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0
for j in range(m+1):
    dp[0][j] = 0
if s[i-1] == s2[j-1]:
    dp[i][j] = 1 + dp[]
else:
    dp[i][j] = max(dp[i-1][j], [i][j-1])
return dp[m]n[m]