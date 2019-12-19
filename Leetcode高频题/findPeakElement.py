'''
@lsy 2019.12.19

Solution 1:
在数组首尾加入-∞，然后遍历数组，找到峰值

Solution 2：二分法，不是很懂
'''
# Solution 1
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        nums = [-float('inf')] + nums + [-float('inf')]
        for i in range(1, len(nums) -1):
            if nums[i] > max(nums[i-1], nums[i+1]):
                return i - 1

        