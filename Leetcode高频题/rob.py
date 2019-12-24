'''
@lsy 2019.12.24

DP
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], nums[1]
        
        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[:i-1])
            
        return max(dp)