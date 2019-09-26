'''
@lsy  2019.9.26
Binary Search.
直接对min 最大值去二分查找。范围是[max(nums), sum(nums)].
在给定一个最大值时，对数组判断，在这个最大值下，最少能把数组划分为几段。
可以对数组中的值，若当前累加值小于最大值，再继续累加；若超过，则把这个数字划分到下一段。
时间复杂度O(nlog(sum(nums))),一般sum(nums)不超过32位或64位。也就是说时间复杂度最多O(64n)=O(n).
空间复杂度O(1).

TODO:
记忆化搜索；DP。
'''
class Solution:
    def subarrayNums(self, nums, largest_sum):
        cnt = 1
        cur_sum = 0
        for n in nums:
            if cur_sum + n <= largest_sum:
                cur_sum += n
            else:
                cur_sum = n
                cnt += 1
        return cnt
    
    def splitArray(self, nums: List[int], m: int) -> int:
        if len(nums) == m:
            return max(nums)
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.subarrayNums(nums, mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left
