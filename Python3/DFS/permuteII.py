# -*- coding:UTF-8 -*-
'''
Solution 1:
- 参考Disscus高票答案
- 题目与https://leetcode.com/problems/permutations/类似，这里多了重复元素，要对重复元素进行处理；
- 这里把nums中的数字一个个插入到已有的path里去，当遇到重复元素，绝不在重复元素后面插入，立刻break；
- 原因还没有想明白！！！
'''

# Solution 1
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        for n in nums:
            temp_res = []
            for path in res:
                for i in range(len(path) + 1):
                    temp_res.append(path[:i]+[n]+path[i:])
                    if i < len(path) and path[i] == n:    break
            res = temp_res
            
        return res
        