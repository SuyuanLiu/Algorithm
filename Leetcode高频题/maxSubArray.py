'''
@lsy 2019.11.12

Solution 1: 数组前缀和
设置prefixSum，计算到第i个数字为止的和。
    prefixSum[j] - prefixSum[i] 表示 nums[i] + ... + nums[j-1]
    第一个位置要插入 0. 对于 nums = [1,2] 的情况。
遍历prefixSum，可以使用两层遍历（超时），这边使用minSum记录出现过的最小的sum。
时间复杂度O(n)

Solution 2: DP
dp[i]表示以nums[i]为结尾的最大的子串和。
公式：dp[i] = dp[i-1] + nums[i] if dp[i-1] >= 0 else nums[i]
结果：max(dp)
时间复杂度O(n)
'''
# Solution 1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        prefixSum = [0]
        for n in nums:
            tmp = n + prefixSum[-1]
            prefixSum.append(tmp)
                
        maxSum = prefixSum[1]
        minSum = prefixSum[0]
        for i in range(1, len(prefixSum)):
            maxSum = max(maxSum, prefixSum[i] - minSum)
            if prefixSum[i] < minSum:
                minSum = prefixSum[i]
                
        return maxSum
        
# Solution 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] >= 0 else nums[i]
        
        return max(dp)
        