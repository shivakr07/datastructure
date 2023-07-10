#  this is the second pattern of dp in strings

# ---------------------------------------------------
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n, m = len(s), len(t)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        # initialize 
        for i in range(n+1):
            dp[i][0] = 1
        # for j in range(1, m+1): #we start j from 1 as already written for 0 otherwise overwrite it 
        #     dp[0][j] = 0
        # we don't need this here because everything is already 0
        # it'll we require if we take -1 
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]
    
# ->can be space optimized it  ?
# -------------------------------------------------------------------
# -> space optimized (SO)
#  we just require previous row values
# because for each i we are running m times so j will be changed for 
# each time -> prev[m+1]
# and for cur we need prev so cu[m+1]
# base case
# for i in range(n+1):
#             dp[i][0] = 1
#  this line just going to each row and assigning 1 at j = 0 so
# in cur and prev we can assign 1 at 0 th postion(oth col)


class Solution:
    def numDistinctSO(self, s: str, t: str) -> int:
        
        n, m = len(s), len(t)
        prev = [0 for i in range(m+1)]
        cur = [0 for i in range(m+1)]
        # initialize 
        prev[0] = cur[0] = 1
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    cur[j] = prev[j-1] + prev[j]
                else:
                    cur[j] =  prev[j]
        return prev[m]
    