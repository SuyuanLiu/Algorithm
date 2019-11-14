'''
@lsy 2019.11.14

简单DP
二维数组dp[i][j]表示从左上角走到(i,j)一共有多少种方法。
初始化：第一行和第一列都是1.
公式：dp[i][j] = dp[i-1][j] +dp[i][j-1]

时间复杂度O(m*n)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] +dp[i][j-1]
                
        return dp[-1]