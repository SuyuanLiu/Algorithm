# -*- coding:UTF-8 -*-
'''
Solution: 动态规划

Solution 1: 时间复杂度O(n^2),空间复杂度O(n)
- 定义一个与nums长度相同的数组dp；
- dp[i]表示的是必须以nums[i]为结尾的最长递增子序列；
- dp[i]的值是，前i-1个数中，小于nums[i]并且长度最大的那个加1；

Solution 2:
https://blog.csdn.net/wbin233/article/details/77570070

'''
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        dp = []
        for i in range(len(nums)):
            max_len = 0
            for j in range(i):
                if nums[i] > nums[j] and dp[j] > max_len:
                    max_len = dp[j]
            dp.append(max_len + 1)

        return max(dp)