# -*- coding:UTF-8 -*-   
'''

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
        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif nums[mid] <= nums[end]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
                    
    return -1        