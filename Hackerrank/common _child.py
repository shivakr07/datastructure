def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)
    # return fun(n-1, m-1, dp)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

# --------------------------------------------------------
# NOTE
"""
this is the basic / totally LCS question but
-> it didn't supported memoization so tabulation is needed otherwise everything is good
"""