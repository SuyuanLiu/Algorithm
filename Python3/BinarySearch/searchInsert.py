# -*- coding:UTF-8 -*-
'''
Solution:
- 二分法
- 注意判断边界条件

'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        res = -1
        while start < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
                
        if start >= end and res == -1:
            if target > nums[start]:
                res = start + 1
            else:
                res = start 
                
        return res
        
                
        