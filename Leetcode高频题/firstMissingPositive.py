'''
@lsy 2019.11.8
两次遍历。
把数字放到对应的下标位置去。即把nums[i] 放到下标为 nums[i]-1的位置去。
第二次遍历，去看对应的下标位置是否放置了应该放置的数字。
时间复杂度O(n)
'''
class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
