# -*- coding:UTF-8 -*-
'''
Solution 1:
- DP, 时间复杂度 O(n^2)
- dp[i] 表示从开始位置能否到达第i个位置；
- 动态方程：dp[i] = i前面能跳到i位置，并且那个位置是开始位置可达的；
- 初始状态：dp[0] = True，注意如果nums[0] = 0的话，任何位置都是False
Tips:
for j in range(i-1, -1, -1) 替代 for j in range(i)
因为如果这个数组所有的数字都是1，从0开始查找太耗时间了。

Solution 2: 
- 贪心， O(n)
- 维护一个变量maxRearchOut，表示从当前位置所能达到的最远的距离
- i <= maxRearchOut,只有满足这个条件，才能继续在maxRearchout这个距离内往前移动i，使得有可能到达更远的距离；
  如果不满足这个条件，也就是说从起始位置无法到达i这个点了，更不用说后面其他的点了，maxRearchOut就不再更新；
  最后比较一下maxRearchOut，看是否能到达数组尾端即可。

'''
# Solution 2
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        
        maxRearchOut = 0
        for i in range(len(nums)):
            if i <= maxRearchOut:
                maxRearchOut = max(maxRearchOut, nums[i]+i)
            
        return maxRearchOut >= len(nums) - 1
            


# Solution 1
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        if nums[0] == 0:
            return False
        
        dp = [False for i in range(len(nums))]
        dp[0] = True
        
        for i in range(1, len(nums)):
            # for j in range(i):              # use this, can't pass all leetcode tests
            for j in range(i-1, -1, -1):
                if nums[j] >= (i-j) and dp[j]:
                    dp[i] = True
                    break
        
        return dp[-1]
