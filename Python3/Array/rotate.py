# -*- coding:UTF-8 -*-
'''
Solution:
- 三步翻转法
- 先把一部分翻转，再把另一部分翻转，最后把全部翻转即可；
- 这里注意判断k = k % len(nums)
'''
class Solution:
    def _reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i, j = i + 1, j - 1
        
    
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k:
            self._reverse(nums, 0, len(nums)-k-1)
            self._reverse(nums, len(nums)-k, len(nums)-1)
            self._reverse(nums, 0, len(nums)-1)
