# -*- coding:UTF-8 -*-
'''
Solution:
- DP超时，使用贪心算法，greedy
- 维护三个变量，step，maxReach，curReach
  step：走到位置i所需的步数
  maxReach：到位置i，所能到达的最远路径
  curReach：表示到上一次，所能走到的最远路径，如果发现curReach < i，
  说明上次的最远路径到不了当前位置i，那么step必须再走一步，同时curReach变为maxReach，也就是到位置i所能达到的最远路径；
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        step = 0
        maxReach, curReach = 0, 0
        for i in range(len(nums)):
            if curReach < i:
                step += 1
                curReach = maxReach
                
            maxReach = max(maxReach, nums[i] + i)
        
        return step
