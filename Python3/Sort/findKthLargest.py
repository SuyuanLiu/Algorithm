# -*- coding:UTF-8 -*-
'''
Solution 1:快排
- random.shuffle(nums)把数组打乱
- 时间复杂度最好是O(n),最坏是O(n^2)(在数组有序的情况下)

Solution 2: 大根堆

Solution 3: 小根堆
'''
# Solution 3
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = [-float('inf') for i in range(k)]
        heapq.heapify(min_heap)
        
        for n in nums:
            if n > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, n)
                
        return min_heap[0]
    


# Solution 2
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-n for n in nums]
        res = float('inf')
        heapq.heapify(nums)
        
        for i in range(k):
            res = heapq.heappop(nums)
            
        return -res
    


# Solution 1
class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def partition(self, nums, start, end):
        p = start
        for i in range(start, end):
            if nums[i] < nums[end]:
                self.swap(nums, p, i)
                p += 1
        self.swap(nums, p, end)
        
        return p
            
        
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        k = len(nums) - k
        start, end = 0, len(nums)-1
        
        while start < end:
            p = self.partition(nums, start, end)
            if p == k:
                break
            elif p < k:
                start = p + 1
            else:
                end = p - 1
        return nums[k]
        
            
        
        