# -*- coding:UTF-8 -*-   
'''
Solution 1:
- 二分，时间复杂度O(logN)
- 首先看mid是否等于target，相等则返回对应下标；不等的话：
    - 如果nums[start] <= nums[mid],说明左半段有序，判断target是否在这个区间内；
    - 否则说明右半段有序，判断target是否在这个区间内；
注：
- 边界条件的判断，<= 等的等于号啥的；
- 一个有序数组从某个点旋转，一定至少有一侧是有序的(可以自己画图看一下)；

Solution 2:
- 二分法
- 与Solution 1是相同的思路，使用模板，不必考虑 <=, +1之类的问题；
           /
         o  M 
       /                                                  
     /                                                  
   / S                                                 
-----------------------------                       
                / E                                
              /                                 
            /                                 
       M  o
        /    
- 设点S为start，E为end， M为二分时的中点mid                            
- 二分时mid有可能在第一段上升区间内，也可能在第二段上升区间内；
  假设mid在第一段上升区间(nums[mid] > nums[-1]), 如果target在 [S,M] 之间，令end=mid；否则start=mid；
  同理对于mid在第二段上升区间；

- 如果不用上述思路，直接用target与nums[mid]进行比较，target < nums[mid]，有可能在[S,M] 之间，也有可能在下面那段上升区间内；

Follow up：
Question：如果数组中有重复的值？
Solution：for loop。（解答见Leetcode 81题）
'''   
# Solution 2
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[-1]:
                if nums[0] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[-1]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

# Solution 1   
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums)-1 
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                       
        return -1              
