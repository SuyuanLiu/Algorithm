# -*- coding:UTF-8 -*-
'''
Solution 1: 
- DP, TC--O(n^2), SC--O(n^2)
- 自顶向下的方法，dp[i][j]表示从顶点走到位置i,j所走的最小路径；
- dp[i][j] = min(dp[-1][j-1], dp[-1][j]) + triangle[i][j]
  注意判断边界条件，当j==0，或者j==n-1的情况。

Solution 2:
优化空间。
发现dp[i][j]的值只与上一层的值相关，因此dp只需要两层即可。
利用 %2 就可以每次对不同的层进行操作。

Solution 3:(TODO)
自底向上。
- dp[i][j]表示从i，j出发走到最后一层的路径最小和。
'''
# Solution 2
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        dp = [[float('inf') for j in range(len(triangle[-1]))] for i in range(2)]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            for j in range(n):
                if j == 0:
                    dp[i%2][j] = dp[1-i%2][0] + triangle[i][j]
                elif j == n - 1:
                    dp[i%2][j] = dp[1-i%2][j-1] + triangle[i][j]
                else:
                    dp[i%2][j] = min(dp[1-i%2][j-1], dp[1-i%2][j]) + triangle[i][j]
        
        return min(dp[1 - len(triangle)%2])
                
            
        

# Solution 1
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        dp = [triangle[0]]
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            tmp_dp = [0 for p in range(n)]
            for j in range(n):
                if j == 0:
                    tmp_dp[j] = dp[-1][0] + triangle[i][j]
                elif j == n - 1:
                    tmp_dp[j] = dp[-1][j-1] + triangle[i][j]
                else:
                    tmp_dp[j] = min(dp[-1][j-1], dp[-1][j]) + triangle[i][j]
                    
            dp.append(tmp_dp)
        
        return min(dp[-1])
