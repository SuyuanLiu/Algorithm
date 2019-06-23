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
    
s = Solution()
nums = [1,2,3,3,3,3,4,5]
print(s.GetNumberOfK(nums, 3))
