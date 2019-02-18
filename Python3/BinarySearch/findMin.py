# -*- coding:UTF-8 -*-
'''
Solution 
- 二分法
- 这题是关于rotated array，首先要先画出rotated array，
         / 
       /                                                  /
     /                                                  /
   / B                                                /
-----------------------------                       /
                / A                               /
              /                                 /  
            /                                 /
          /                                 /

有两种情况，左侧rotated，右侧是极端情况，没有rotated（也是rotated的一种情况）
看左侧的图可以看出来，右下角的数值严格小于左半部分的数值，因此有两个点A，B；
    - 对于点A (nums[end])，翻转点右侧值都小于A，翻转点左侧值都大于A；
    - 对于点B (nums[0])，翻转点右侧值都小于B，翻转点左侧值都大于B；
但有一个问题，如果rotated是右侧的情况，即未经翻转，那么点B就不存在了，而A点是一定存在的，所以这边二分利用点A会比较好；
（Solution 1，利用点B进行判断，在遇到未经翻转的数组，最后的判断就比较麻烦了）

Follow up:
Question:
数组中存在重复的值，怎么办？154. Find Minimum in Rotated Sorted Array II， https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
Solution：
黑盒测试证明最坏情况是O(n).具体代码见154的解答。

'''
# Solution 2
class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[-1]:
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[-1]:
            return nums[start]
        else:
            return nums[end]
        

# Solution 1
class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[0]:
                start = mid
            else:
                end = mid
                
        if nums[start] < nums[0]:
            return nums[start]
        if nums[end] < nums[0]:
            return nums[end]
        return nums[0]
