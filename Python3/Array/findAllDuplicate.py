# -*- coding:UTF-8 -*-
'''
Solution 1:
- 时间复杂度O(NlogN)，空间复杂度O(1)
- 对数组排序（快排），遍历一遍数组即可找到重复数字；

Solution 2：
- 时间复杂度O(N)，空间复杂度O(1)
- 由于数组长度为n+1,数组中数值范围为1-n,那么数组中数值减1后一定可作为数组下标；
- 思想：把数组中数值（减1）做为数组下标，如果有重复的值，那么他们一定会指向同一个下标；
  要找出那些出现个两次的值，就要对他们进行标记：
  遍历数组，把nums[nums[i]]变为负数；如果nums[nums[i]]已经是负数，说明在这之前已经指向过这个值了，也就是说nums[i]就是重复值；
 
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


# Solution 2:
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(abs(nums[i]))
            else:
                nums[idx] *= -1
        
        return res