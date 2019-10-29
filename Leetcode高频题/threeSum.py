'''
@lsy 2019.10.29

对数组排序。
对数组外层循环到nums[i]，然后在内层使用双指针找到两数之和等于-nums[i]。
要注意结果可能出现重复的情况，要对当前数值进行判断，如果连续几个数值都相同，则直接++。
时间复杂度O(n^2)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p, q = i + 1, len(nums) - 1
            while p < q:
                _sum = nums[p] + nums[q] + nums[i]
                if _sum > 0:
                    q -= 1
                elif _sum < 0:
                    p += 1
                else:
                    res.append([nums[i], nums[p], nums[q]])
                    while p < q and nums[p] == nums[p+1]:
                        p += 1
                    while p < q and nums[q] == nums[q-1]:
                        q -= 1
                    p += 1
                    q -= 1

        return res
        