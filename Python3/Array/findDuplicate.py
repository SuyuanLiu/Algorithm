# -*- coding:UTF-8 -*-
'''
Solution 1:
- 时间复杂度O(NlogN)，空间复杂度O(1)
- 对数组排序（快排），遍历一遍数组即可找到重复数字；

- 这个方法能够找到所有的重复数字，但这个方法修改了数组，不符合题目要求....

Solution 2：
- 利用二分思想，时间复杂度O(NlogN)，空间复杂度O(1)；
- 假设数组中数值范围为1~n,取中间值 mid=(1+n)/2, 遍历数组，看数组中数值在 [1,mid] 范围内的数有几个；
  如果个数超过mid-1+1，说明重复数值一定在 [1,mid] 范围内，否则在 [mid+1, n] 范围内；
  如果在[1, mid]内，再对它二分，重复以上操作直到找个找个数值；

- 这个方法不能找出所有的重复数值；

Solution 3:
- 双指针，时间复杂度O(N)，空间复杂度O(1)；
- 思想与“寻找有环链表环的入口”一样；
- 由于数组长度为1+n,数组数值大小为1—n，所以可以把数组看成类似链表的结构，nums[i] 指向下标为nums[i]的位置。
  如果有重复的数，那么一定会形成一个环（重复的数值总会指向相同的下标位置）；
  因为：如果没有重复的值，每个nums[i]都指向一个单独的下标，不会有重复的指向。
- 定义两个指针，快慢指针，一个一次一步，一个一次两步，最终相遇；找到环入口，让快指针从头开始，快慢指针一起走，再次相遇就是环入口；

- 这个方法同样不能找出所有的重复数值。
'''


# Solution 1
class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums
    
    def quickSort(self, nums, start, end):
        s = start
        if start >= end:
            return nums
        p = start
        while start < end:
            if nums[start] < nums[end]:
                nums = self.swap(nums, start, p)
                p += 1
            start += 1
        nums = self.swap(nums, end, p)
        
        nums = self.quickSort(nums, s, p-1)
        nums = self.quickSort(nums, p+1, end)
        
        return nums
        

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        
        nums = self.quickSort(nums, 0, len(nums)-1)
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]




# Solution 2
class Solution:
    def binaryFindDuplicate(self, nums, l, r):
        if l >= r:
            return l
        
        mid = (l + r) // 2
        cnt = 0
        for i in range(len(nums)):
            if l <= nums[i] <= mid:
                cnt += 1
        
        if cnt > (mid - l + 1):
            return self.binaryFindDuplicate(nums, l, mid)
        else:
            return self.binaryFindDuplicate(nums, mid+1, r)

    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        
        return self.binaryFindDuplicate(nums, 1, len(nums)-1)
        

# Solution 3
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow