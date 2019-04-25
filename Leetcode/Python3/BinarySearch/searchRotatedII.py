# -*- coding:UTF-8 -*-
'''
Solution:
- 二分，时间复杂度O(n)
- 基本处理情况类似searh in rotated sorted array, 总是至少一侧有序，另外需要特殊考虑元素重复的情况；
- 如果发现 nums[start] == nums[mid]，就把start加1，相当于去掉重复元素的影响；
- 然后再判断是哪一侧有序，判断target是否在有序的那一侧；
- 对重复元素的解决办法就是移动边缘指针，相当于去掉影响有序判读的重复元素，导致每次不能去掉一半的元素，导致时间复杂度增加到O(N).

Solution 2:
- for loop, 遍历
'''
# Solution 2
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'bool':
        for n in nums:
            if n == target:
                return True
        return False
        

# Solution 1
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return True
            if nums[start] == nums[mid]:
                start += 1
                continue
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:  
                    end = mid - 1
        return False
