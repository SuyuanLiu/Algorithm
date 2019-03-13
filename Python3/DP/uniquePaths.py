# -*- coding:UTF-8 -*-
'''
Solution:
- DP
- dp[i][j] 表示走到i,j位置，一共有多少种方法
- 动态方程：
  dp[i][j] = dp[i-1][j] + dp[i][j-1]
- 初始化：第一行和第一列都是只有一种方式，都初始为1。
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for j in range(n)] for j in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]
