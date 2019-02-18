# -*- coding:UTF-8 -*-
'''
Solution:
- for循环遍历一遍，O(n)
- 这是 153. Find Minimum in Rotated Sorted Array 的follow up。
     (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- 
'''
class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        minN = nums[0]
        for n in nums:
            minN = min(minN, n)
            
        return minN
