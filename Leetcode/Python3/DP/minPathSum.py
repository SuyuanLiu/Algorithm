# -*- coding:UTF-8 -*-
'''
Solution:
- DP
- dp[i][j]表示走到i,j所需的最短路径。
- 动态方程：
  dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
- 初始状态：第一行和第一列要初始化
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return
        
        row, col = len(grid), len(grid[0])
        dp = [[0 for j in range(col)] for i in range(row)]
        
        for i in range(col):
            dp[0][i] = grid[0][i] + dp[0][i-1] if i != 0 else grid[0][i]
        for i in range(1, row):
            dp[i][0] = grid[i][0] + dp[i-1][0] 
            
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]
