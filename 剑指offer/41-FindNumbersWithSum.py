'''
解题思路：
- 数组已经排好序了
- 使用双指针，分别指向头/尾指针，判断二者之和
  如果大于target，尾指针向前移
  如果小于target，头指针向后移
- 若两指针相遇，则不存在和为target的一组数

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 存在这组数/不存在这组数
- 空数组
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, nums, target):
        # write code here
        if not nums:
            return []
         
        res = []
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                if not res:
                    res.append(nums[i])
                    res.append(nums[j])
                elif nums[i] * nums[j] < res[0] * res[1]:
                    res[0],res[1] = nums[i], nums[j]
                i, j = i + 1, j - 1
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
        return res
