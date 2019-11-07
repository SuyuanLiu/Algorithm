'''
@lsy 2019.11.7
二分搜索
做两次二分搜索，分别找到起点和终点。

一定注意二分搜索的边界问题！！！

看leetcode自己之前提交的代码，之前有两种写法，之后研究一下。
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        start, end = -1, -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                high = mid - 1
                start = mid
                
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
                end = mid 
                
        return [start, end]
                
                
        