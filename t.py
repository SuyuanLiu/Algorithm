# -*- coding:utf-8 -*-
class Solution:
    def merge(self, nums, start, end, mid):
        A, cnt = [], 0
        i, j = mid, end
        # import pdb; pdb.set_trace()
        while i >= start and j > mid:
            if nums[i] > nums[j]:
                A.append(nums[i])
                i -= 1
                cnt += j - mid
            else:
                A.append(nums[j])
                j -= 1
        if i >= start:
            A = A + nums[start:i+1][::-1]
        if j > mid:
            A = A + nums[mid+1:j+1][::-1]
        nums = nums[:start] + A[::-1] + nums[end+1:]
        return nums, cnt
        
    def mergeSort(self, nums, start, end):
        if start >= end:
            return nums, 0
        mid = start + (end - start) // 2
        nums, lcnt = self.mergeSort(nums, start, mid)
        nums, rcnt = self.mergeSort(nums, mid+1, end)
        nums, cnt = self.merge(nums, start, end, mid)
        return nums, lcnt + rcnt + cnt
    
    def InversePairs(self, nums):
        # write code here
        if len(nums) < 2:
            return 0
        nums, cnt = self.mergeSort(nums, 0, len(nums)-1)
        return cnt
    
s = Solution()
nums = [1,2,3,4,5,6,7,0]
print(s.InversePairs(nums))
