'''
@lsy 2019.10.25

Solution: DP

时间复杂度O(nxm)，空间复杂度O(nxm)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False for j in range(m+1)] for i in range(n+1)]
        
        dp[0][0] = True
        for j in range(1, m+1):
            dp[0][j] = dp[0][j-2] if p[j-1] == '*' else False
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == '.' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]

                    
        return dp[-1][-1]