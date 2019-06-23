'''
解题思路：
- 归并排序
- 在归并过程中，两个有序数组A，B，从末尾开始比较，如果A的尾大于B的尾，那么A尾对B中所有数字构成逆序对；然后向前移动并比较即可。

时空复杂度：
- 时间复杂度 O(nlogn)
- 空间复杂度 O(n)

Test Cases：
- 未经排序的数组，已经排好序的数组（递增/递减），数组中有重复数字
- 空数组，只有一个数值，只有两个数值

'''
# -*- coding:utf-8 -*-
# 跑了好几次才通过
class Solution:
    def mergeSort(self, copy, nums, start, end):
        if start >= end:
            return 0
        mid = start + (end - start) // 2
        cnt = self.mergeSort(nums, copy, start, mid) + self.mergeSort(nums, copy, mid+1, end)
        
        i, j = mid, end
        idx = end
        while i >= start and j > mid:
            if nums[i] > nums[j]:
                cnt += j - mid
                copy[idx] = nums[i]
                i -= 1
            else:
                copy[idx] = nums[j]
                j -= 1
            idx -= 1
        while i >= start:
            copy[idx] = nums[i]
            i, idx = i - 1, idx - 1
        while j > mid:
            copy[idx] = nums[j]
            j, idx = j - 1, idx - 1
        return cnt
    
    def InversePairs(self, nums):
        # write code here
        if len(nums) < 2:
            return 0
        return self.mergeSort(nums[:], nums[:], 0, len(nums)-1)%1000000007



# 25%
class Solution:
    def InversePairs(self, nums):
        # write code here
        if not nums:
            return 0
        
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1
        return cnt



# 50%
class Solution:
    def InversePairs(self, nums):
        # write code here
        if not nums:
            return 0
        
        cnt = 0
        while nums:
            idx = nums.index(min(nums))
            cnt += idx
            nums.remove(nums[idx])
        return cnt

# 75%
class Solution:
    def merge(self, nums, start, end, mid):
        A, cnt = [], 0
        i, j = mid, end
        while i >= start and j > mid:
            if nums[i] > nums[j]:
                A.append(nums[i])
                i -= 1
                cnt += j - mid
            else:
                A.append(nums[j])
                j -= 1
        while i >= start:
            A.append(nums[i])
            i -= 1
        while j > mid:
            A.append(nums[j])
            j -= 1
        
        idx = len(A) - 1
        for i in range(start, end+1):
            nums[i] = A[idx]
            idx -= 1
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
        return cnt%1000000007
