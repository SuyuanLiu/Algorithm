'''
@lsy 2019.10.31

设置pre_num, pre_pos来记录上一个数字和上一个位置。
遍历数组，当当前值与上一个数字不相同时，对pre_pos+1的位置更新数值，同时更新pre_num.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return len(nums)
        
        pre_num, pre_pos = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] != pre_num:
                pre_pos += 1
                nums[pre_pos] = nums[i]
                pre_num = nums[i]
        return pre_pos + 1