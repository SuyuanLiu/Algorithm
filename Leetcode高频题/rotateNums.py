'''
@lsy 2019.12.23

将前面翻转，后面翻转，然后整体翻转。
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < 1 or not nums:
            return nums
        
        k = k % len(nums)
        
        def reverseNums(start, end):
            if len(nums) < 2:
                return 
            i, j = start, end
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
                
        reverseNums(0, len(nums)-k-1)
        reverseNums(len(nums)-k, len(nums)-1)
        reverseNums(0, len(nums)-1)
        