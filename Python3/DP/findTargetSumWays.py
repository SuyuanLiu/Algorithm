# -*- coding:UTF-8 -*-
'''
Solution 1: DP, TC-O(NC), SC-O(C)
- !!! (这种方法在数字值非常大的时候很耗空间，没有通过LeetCode测试)
- 转换为0-1背包问题
- 把列表中的数分为两部分，P(positive), N(negative)，有如下推导：
  sum(P) - sum(N) = target
  sum(P) - sum(N) + sum(P) + sum(N) = target + sum(nums)
  2sum(P) = target + sum(nums)
- 也就是要找一个子集，使得其和为 n = (target + sum(nums)) / 2. 
- 定义一个数组dp[len(nums)+1][n+1]，其中dp[i][j]指的是前i个值中组成和为j的方法数，那么
  dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]  (前i-1个数组成j-n的方法数(用nums[i-1]) + 前i-1组成j的方法数)
- 注意使用一维的dp时，要倒着更新，防止被覆盖。


Solution 2: DP
- 参考高票答案
- 
'''
# Solution 2
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if (sum(nums) + S) % 2:
            return 0
        
        if nums[0] != 0:
            dic = {nums[0]:1, -nums[0]:1}
        else:
            dic = {0:2}
            
        for i in range(1, len(nums)):
            temp_dict = {}
            num = nums[i]
            for d in dic:
                temp_dict[d+num] = temp_dict.get(d+num, 0) + dic.get(d, 0)
                temp_dict[d-num] = temp_dict.get(d-num, 0) + dic.get(d, 0)
            dic = temp_dict
            
        return dic.get(S, 0)


# Solution 1
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if (sum(nums) + S) % 2:
            return 0
        
        n = (sum(nums) + S) // 2
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        
        for i in range(1, len(nums)+1):
            for j in range(n, 0, -1):
                if j >= nums[i-1]:
                    dp[j] += dp[j-nums[i-1]]
                    
        return dp[n]
                
                