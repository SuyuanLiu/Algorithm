# -*- coding:UTF-8 -*-
'''
Solution:
- 双指针
'''
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
