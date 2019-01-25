# -*- coding:UTF-8 -*-
'''
Solution: DP
- dp[i] = dp[i-1] + dp[i-2]

Solution 2:
- 优化空间，dp[i]只与dp[i-1],dp[i-2]相关，可以用两个变量把他们存下来；
'''
# Solution 2
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        
        n1, n2 = 1, 2
        res = 0
        while n - 2:
            res = n1 + n2
            n1 = n2
            n2 = res
            n -= 1
            
        return res
        


# Solution 1
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        
        dp = [0 for i in range(n+1)]
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]
        