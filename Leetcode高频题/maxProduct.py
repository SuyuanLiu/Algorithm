'''
@lsy 2019.12.6
记录以当前数字为结尾的最大、最小子数组的乘积。
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        
        imax, imin, res = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            tmp = imax
            imax = max(imax * n, imin * n, n)
            imin = min(tmp * n, imin * n, n)
            
            res = max(imax, res)
            
        return res