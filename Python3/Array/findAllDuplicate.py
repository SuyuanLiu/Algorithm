# -*- coding:UTF-8 -*-
'''
Solution 1:
- 时间复杂度O(NlogN)，空间复杂度O(1)
- 对数组排序（快排），遍历一遍数组即可找到重复数字；

Solution 2：

'''

# Solution 1
class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums
    
    def quickSort(self, nums, start, end):
        s = start
        if start >= end:
            return nums
        p = start
        while start < end:
            if nums[start] < nums[end]:
                nums = self.swap(nums, start, p)
                p += 1
            start += 1
        nums = self.swap(nums, end, p)
        
        nums = self.quickSort(nums, s, p-1)
        nums = self.quickSort(nums, p+1, end)
        
        return nums
    
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        nums = self.quickSort(nums, 0, len(nums)-1)
        res = []
        
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
                while i < len(nums) and nums[i] == nums[i-1]:
                    i += 1
            else:
                i += 1
                
        return res