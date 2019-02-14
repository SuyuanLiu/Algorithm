# -*- coding:UTF-8 -*-
'''
Solution:二分法
- 使用模板，先找到target出现的第一个位置，然后再从第一个出现的位置往后面去找，直到找到最后一个位置；
- 或者可以做两次二分，分别找到第一次出现的位置和最后一次出现的位置；
'''
# Solution 1
class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if not nums:
            return [-1, -1]
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
                
        l, r = -1, -1
        if nums[start] == target:
            l, r = start, start
        elif nums[end] == target:
            l, r = end, end
        
        while r+1 < len(nums) and nums[r+1] == target:
            r += 1
        return [l, r]

# Solution 2
class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if not nums:
            return [-1, -1]
        
        l, r = -1, -1   
        # First Position
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            l= start
        elif nums[end] == target:
            l= end
            
        # Last Position    
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                start = mid
        if nums[end] == target:
            r= end
        elif nums[start] == target:
            r= start
            
        return [l,r]
