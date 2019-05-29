'''
解题思路：
Solution 1
- 借助前缀和
- 建立一个数组preSum，下标为i的存放这前i位数字之和，preSum[j] - preSum[i] 就表示第j个到第i个子数组之和
- 内部一个双层循环，遍历preSum即可
注意：preSum的第一个数字放入0，这样preSum[j] - preSum[0] 就可以表示从最开始到第j个数字之和

时间复杂度 O(n^2)，空间复杂度 O(n)

--------------------------------------------------
Solution 2
动态规划
- 建立一个等长数组res，第i个元素表示以nums[i]结尾的最大的和
- res[i] = nums[i], if i == 0 or res[i-1] <= 0
         = res[i-1] + nums[i], else
- 最后结果是max(res)

时间复杂度 O(n)，空间复杂度 O(n)

------------------------------------------------
Test Cases：
- 空数组
- 全是负数，全是正数，有正有负

'''
# -*- coding:utf-8 -*-
# Solution 1
class Solution:
    def FindGreatestSumOfSubArray(self, nums):
        # write code here
        if not nums:
            return 0
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1] + n)
            
        maxSum = preSum[1]
        for i in range(len(preSum)):
            for j in range(i+1, len(preSum)):
                tmp = preSum[j] - preSum[i]
                maxSum = max(maxSum, tmp)
        return maxSum



# Solution 2
class Solution:
    def FindGreatestSumOfSubArray(self, nums):
        # write code here
        if not nums:
            return 0
        res = [nums[i] for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0 or res[i-1] <= 0:
                res[i] = nums[i]
            else:
                res[i] = res[i-1] + nums[i]
        return max(res)
