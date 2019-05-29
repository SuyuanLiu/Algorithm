'''
解题思路：
Solution 1:
基于快排的思想，利用partition。
- 每次partition，判断分割点的位置是否是第k个，是的话直接返回前k个数字即可；
- 若分割点位置在k前面，继续分割后面的部分，直到找到k
- 若分割点位置在k后面，则分割前面部分

平均时间复杂度O(n)，空间复杂度O(1)，适用于数据不是很大的情况。

注意：如果数组基本有序，最好打乱一下顺序

-----------------------------------------------------------
Solution 2:
利用堆
- 建立一个最大堆即可
- python的heapq是最小堆，对数组取负即可

平均时间复杂度O(nlogk)，空间复杂度O(k)，适用于数据量很大，k比较小的情况。

---------------------------------------------------------
Test Cases：
- 空数组
- k = 0
- k > len(nums)
- k = len(nums)
- 一般用例

⚠️
- 询问特殊情况的处理方式，比如k = 0，k > len(nums)，输出什么
- 输出是否需要排序(牛客上要求排好序)
- 询问数据量情况
'''
# -*- coding:utf-8 -*-
# Solution 1
class Solution:
    def partition(self, nums, k, start, end):
        p = start 
        for i in range(start, end):
            if nums[i] < nums[end]:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[end], nums[p] = nums[p], nums[end]
        if p == k - 1:
            return nums[:p+1]
        elif p < k - 1:
            return self.partition(nums, k, p+1, end)
        else:
            return self.partition(nums, k, start, p-1)
    
    def GetLeastNumbers_Solution(self, nums, k):
        # write code here
        if len(nums) < k or k == 0:
            return []
        if len(nums) == k:
            nums.sort()
            return nums
        res = self.partition(nums, k, 0, len(nums)-1)
        res.sort()
        return res


# Solution 2
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
