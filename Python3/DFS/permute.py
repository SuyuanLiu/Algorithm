# -*- coding:UTF-8 -*-
'''
Solution: DFS(BackTracking)
- 定义dfs函数，res存放最终结果，permutation前几位可能的结果；
'''

class Solution:
    def dfs(self, nums, res, permutation):
        if len(nums) == 1:
            res.append(permutation+nums)
        else:
            for i in range(len(nums)):
                res = self.dfs(nums[:i]+nums[i+1:], res, permutation+[nums[i]])
        return res
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        return self.dfs(nums, [], [])
        