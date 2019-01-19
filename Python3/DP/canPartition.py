# -*- coding:UTF-8 -*-
'''
Solution: DP

0-1背包问题，这题就是看能否找到几个数，使得它们的和为sum/2.abs

Solution 1: TC-O(NS), SC-O(NS)
- 定义一个二维数组 dp[n+1][s+1], 其中 s = sum/2, dp[i][j] 表示的是前i个数中是否能选出和为j的, 能的话为True,不能为False；那么
  dp[i][j] = dp[i-1][j]              ，不需要nums[i]
           = dp[i-1][j-nums[i]]      ，需要nums[i]    (这边需要判断j与nums[i]的大小)

Solution 2: TC-O(NS), SC-O(N)
- 定义一个一维数组dp[n+1], 从上面的分析看出，dp[i][j]的值只与dp[i-1]相关，所以可以用两行的数组来做dp，更进一步只需要一维的数组；
  dp[j]既可以表示dp[i-1][j],也可以表示dp[i][j]，从上一轮的就是dp[i-1][j]，本轮计算就是dp[i][j];
  因为计算需要用到dp[i-1][j-nums[i]]，所以要倒着更新dp[n],防止dp[i-1][j-nums[i]]变成dp[i][j-nums[i]].
'''

# Solution 2
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        
        s, n = sum(nums) // 2, len(nums)
        dp = [False for i in range(s+1)]
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(s, 0, -1):
                if j >= nums[i-1]:
                    dp[j] = dp[j] or dp[j-nums[i-1]]
                    
        return dp[s]
        
        


# Solution 1
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        
        s = sum(nums) // 2 
        n = len(nums)
        
        dp = [[False for j in range(s+1)] for i in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1):
            for j in range(1, s+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[n][s]