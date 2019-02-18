# -*- coding:UTF-8 -*-
'''
Solution:                                           /\  /\ 
- 二分法，时间复杂度O(logn)                           /  \/  \/\ 
- 题目要求时间复杂度是log级别的，可以想到是二分法；      /           \ 
- 题目说明数组两侧认为是 -∞，这表明数组中一定存在峰值； /              \ 
- 对于mid来说有四种情况：(假设中间的点为mid)
         /         o        o   o       \ 
        /         / \        \ /         \ 
       /         o   o        o           \ 
     递增         peak        bottom      递减     
    对于递增，在它的右侧一定会有峰值点；
    对于递减，在它的左侧一定会有峰值点；
    对于bottom，任选一侧即可；
    peak，满足条件；

Additionaly：
- 拿到这个题目，第一反应是遍历一遍数组，时间复杂度是O(n)，这可以找到所有的peak，而题目只要返回任意peak即可，说明有更好的做法；
'''
class Solution:
    def findPeakElement(self, nums: 'List[int]') -> 'int':
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid
                
        if start == 0 and nums[0] > nums[1]:
            return 0
        return end
