'''
解题思路：
- “41-和为s的两个数字”的扩展
- 两个指针low, high, 从1，2开始
  如果 sum(low ～ high) < target，让序列中包含更多的数字，即high向后移动
  如果 sum(low ~ high) > target, 从序列中去掉较小的值，即把low向后移动
- 终止条件是 low >= high (有点不太理解)，剑指 offer上写是 low >= (1+target)/2，因为序列至少要包含两个数字；

Test Cases：
- 存在和为s的连续序列(9,100)
- 不存在和为s的连续序列(0,4)
- 边界测试，s=3
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, target):
        # write code here
        res = []
        low, high = 1, 2
        while low < high:
            tmp = (low + high) * (high - low + 1) // 2
            if tmp == target:
                res.append([n for n in range(low, high+1)])
                low += 1
            elif tmp < target:
                high += 1
            else:
                low += 1
        return res
