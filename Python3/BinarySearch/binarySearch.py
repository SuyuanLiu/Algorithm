# -*- coding:UTF-8 -*-
'''
Solution:
- 非递归和递归
- 主要思想：将target与数组中间的值进行比较，target == nums[mid], 则返回对应下标；
                                        target > nums[mid]， 说明只能在右侧寻找；
                                        target < nums[mid]， 说明只能在右侧寻找；
- 时间复杂度：O(logN), 递归算法额外使用了栈的信息；
'''

class Solution(object):
    # Solution 1: non-recursion
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    


    # Solution 2: recursion
    def binarySearch(self, nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(nums, start, mid-1, target)
        else:
            return self.binarySearch(nums, mid+1, end, target)
    
    
    def search(self, nums, target):
        return self.binarySearch(nums, 0, len(nums)-1, target)
    

        