'''
@lsy 2019.11.15

DP
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]
        