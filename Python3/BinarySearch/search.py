# -*- coding:UTF-8 -*-
'''
Question：
给定有序数组nums,其中不含有重复元素，请找到满足nums[i]==i条件的最左的位置。
如果所有位置上的数都不满足条件，返回-1.

Solution：
- 二分搜索；
- 首先定义res = -1, 然后利用二分搜索，如果nums[i] > i, 那么结果在i的左侧，因为整数的增幅最小是1，i的增幅严格为1，右侧不可能存在相等情况；
                                      若nums[i] < i, 那么结果在i的右侧;
                                      若nums[i] == i，把i赋值给res,然后继续搜索左侧，因为要找的是最左的位置；                                   
- 如果存在以下两种特殊情况，直接返回-1：
    nums[0] > 0 和 nums[n-1] < n-1 （n = len(nums)）                                       
'''
class Solution:
    def search(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        n = len(nums)
        if n == 0 or nums[0] > 0 or nums[n-1] < n-1:
            return -1
        
        res = -1
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) // 2
            if mid == nums[mid]:
                res = mid
                end = mid - 1
            elif mid > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return res