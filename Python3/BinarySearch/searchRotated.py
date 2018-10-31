# -*- coding:UTF-8 -*-   
'''
Solution:
- 二分，时间复杂度O(logN)
- 首先看mid是否等于target，相等则返回对应下标；不等的话：
    - 如果nums[start] <= nums[mid],说明左半段有序，判断target是否在这个区间内；
    - 否则说明右半段有序，判断target是否在这个区间内；
注：
- 边界条件的判断，<= 等的等于号啥的；
- 一个有序数组从某个点旋转，一定至少有一侧是有序的(可以自己画图看一下)；
'''   
   
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums)-1 
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
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
                       
        return -1              