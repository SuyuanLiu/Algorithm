'''
@lsy 2019.11.16

双指针。
p0/p2 分别指向 0/2 所在的最后一个位置。
遍历数组，若当前数字是 0，则与 p0 位置数字进行交换。
注意：
  判断 i < pointer2，要用 <，不要用 !=
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer0, pointer2 = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i > pointer0:
                nums[i], nums[pointer0] = nums[pointer0], nums[i]
                pointer0 += 1
            elif nums[i] == 2 and i < pointer2:
                nums[i], nums[pointer2] = nums[pointer2], nums[i]
                pointer2 -= 1
            else:
                i += 1
