# -*- coding:UTF-8 -*-
'''
Solution:
- 二分法
- 注意判断边界条件

Solution 2:
- 使用模板
- 在最开始时判断target与nums[0],nums[-1]的关系，可以节省时间；
- 最后start，end与target的关系有5种： 
    target==nums[start], target==nums[end], target<nums[start], target>nums[end], nums[start]<target<nums[end].

Solution 3:
- 使用模板
- 分析题目，发现题目可以转化为：find the first number larger than target
                         （或find the last number less than target)
- 如果找不到这个位置，就直接返回len(nums)
'''
# Solution 3: use template(Find first position)
class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return 0
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
                
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        
        return len(nums)

# Solution 2:use template(my own idea)
class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return 0
        
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                end = mid 
            elif target > nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid
                
        if target <= nums[start]:
            return start
        if target > nums[end]:
            return end + 1
        if target == end:
            return end
        return start + 1
        


# Solution 1
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
