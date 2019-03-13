# -*- coding:UTF-8 -*-
'''
Solution:
- DP
- dp[i][j] 表示走到i,j位置，一共有多少种方法
- 动态方程：
  dp[i][j] = dp[i-1][j] + dp[i][j-1]
- 要注意的是，如果该位置为1，那么走到这里的方法数就是0.
- 初始化：第一行和第一列。遇到1之前的方法数都为1，之后的都为0
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(col)] for i in range(row)]
        
        for i in range(col):
            if i == 0:
                dp[0][i] = 1 - obstacleGrid[0][i] 
            elif obstacleGrid[0][i]:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(row):
            if i == 0:
                dp[i][0] = 1 - obstacleGrid[i][0] 
            elif obstacleGrid[i][0]:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
            
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[-1][-1]
