# -*- coding:UTF-8 -*-
'''
Solution: BackTracking 
- 这题是78. Combination，https://leetcode.com/problems/combinations/的扩展；
- 定义函数combineN，用来从数组中选n个数字作为子集；
  定义path保存当前的路径，res存取结果；
'''
class Solution:
    def combineN(self, nums, n, res, path):
        if n == 1:
            for i in range(len(nums)):
                res.append(path + [nums[i]])
        else:
            for i in range(len(nums)-n+1):
                res = self.combineN(nums[i+1:], n-1, res, path+[nums[i]])
                
        return res
        
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        res = [[]]
        
        for i in range(len(nums)):
            res += self.combineN(nums, i+1, [], [])
            
        return res
        
        