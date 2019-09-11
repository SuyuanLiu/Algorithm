'''
@lsy  2019.9.11

动态规划
- 最大值，要么是当前最大值与当前值的乘积，
         要么是当前最小值与当前值的乘积，
         要么是当前值；
- 注意，for循环中，要用tmp变量，因为_max已经发生变化了；

时间复杂度O(n)，空间复杂度O(1)
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        _max, _min = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            tmp = _max
            _max = max(_max * nums[i], _min * nums[i], nums[i])
            _min = min(tmp * nums[i], _min * nums[i], nums[i])
            
            res = max(_max, res)
        return res
