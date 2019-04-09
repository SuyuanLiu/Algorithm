'''
Solution:
- DP
- dp[i][j]表示s的前i个字符表示t的前j个字符有多少种方法
- 状态方程：dp[i][j] = dp[i-1][j-1] + dp[i-1][j], if s[i-1] == t[j-1]
                    = dp[i-1][j]
    dp[i][j]与前i-1个字符表示前j个字符有多少种方法相关
- 初始化：第1列要初始化为1，s的前i个字符表示空串的方式有1种
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]
