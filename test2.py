# -*- coding:utf-8 -*-
import heapq


class Solution:
    def GetLeastNumbers_Solution(self, nums, k):
        # write code here
        if len(nums) < k or k == 0:
            return []
        if len(nums) == k:
            nums.sort()
            return nums
        
        nums = [-n for n in nums]
        res = nums[:k]
        heapq.heapify(res)
        for i in range(k, len(nums)):
            if nums[i] > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, nums[i])
        res = [-n for n in res]
        res.sort()
        return res
