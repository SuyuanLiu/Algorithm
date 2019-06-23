'''
解题思路：
Solution 1:
- 采用二分法，找到数字K，然后往两边找到第一个K与最后一个K。
- 如果数组中有n个K，那么时间复杂度就是O(n)了

Solution 2:
- 二分法，找到第一个K和最后一个K的位置，确定K出现的次数
- 找到第一个K的位置：当二分法nums[mid] == K，要判断当前mid位置是否为第一个K，如果mid-1位置也是K，说明第一个K在前半部分，继续在前半部分二分。
- 时间复杂度是O(logn)

Test Cases：
- 包含查找数字（出现多次/一次），不包含查找数字
- 空数组

'''
# Solution 1
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        start, end = 0, len(data) - 1
        cnt = 0
        while start <= end:
            mid = (end - start) / 2 + start
            if k > data[mid]:
                start = mid + 1
            elif k < data[mid]:
                end = mid - 1
            else:
                cnt = 1
                break
         
        if cnt == 0:
            return cnt
        i = mid - 1
        while i >= 0 and data[i] == k:
            cnt += 1
            i -= 1
        i = mid + 1
        while i < len(data) and data[i] == k:
            cnt += 1
            i += 1
        return cnt

# Solution 2
# -*- coding:utf-8 -*-
class Solution:
    def getFirstK(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == k:
                if mid > 0 and nums[mid-1] == k:
                    end = mid - 1
                else:
                    return mid
            elif nums[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
    def getLastK(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == k:
                if mid < len(nums) - 1 and nums[mid+1] == k:
                    start = mid + 1
                else:
                    return mid
            elif nums[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1        
    
    def GetNumberOfK(self, nums, k):
        # write code here
        if not nums:
            return 0
        l = self.getFirstK(nums, k)
        r = self.getLastK(nums, k)
        if l == -1 or r == -1:
            return 0
        return r - l + 1
