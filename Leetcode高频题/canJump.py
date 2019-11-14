'''
@lsy 2019.11.14
贪心。
从当前节点出发所能到达的最远距离，这过程中记录最大的距离reach；
如果 i > reach，说明从开始位置最多走到 reach 位置，不可能走到 i 位置，也就不会再有可能走到 end 了。
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, reach = 0, 0
        while i < len(nums) and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1
        return i == len(nums)