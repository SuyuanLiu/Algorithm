# -*- coding:UTF-8 -*-
'''
Solution 1:
- 时间复杂度O(NlogN)，空间复杂度O(1)
- 对数组排序（快排），遍历一遍数组即可找到重复数字；
- 这个方法能够找到所有的重复数字，但这个方法修改了数组，不符合题目要求....

Solution 2：
- 利用二分思想，时间复杂度O(NlogN)，空间复杂度O(1)；
- 假设数组中数值范围为1~n,取中间值 mid=(1+n)/2, 遍历数组，看数组中数值在 [1,mid] 范围内的数有几个；
  如果个数超过mid-1+1，说明重复数值一定在 [1,mid] 范围内，否则在 [mid+1, n] 范围内；
  如果在[1, mid]内，再对它二分，重复以上操作直到找个找个数值；
- 这个方法不能找出所有的重复数值；
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
        

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        
        nums = self.quickSort(nums, 0, len(nums)-1)
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]