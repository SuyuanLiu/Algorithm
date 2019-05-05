'''
解题思路：
普通思路：直接遍历一遍，时间复杂度O(n)，有更优的方法：二分法。

特殊情况：输入数组为排好序的数组，直接判断当第一个元素小于最后一个元素的话，就说明数组排好序，最小值就是第一个元素。
旋转数组，那么在旋转点划分的两段分别是非递减序列。使用两个指针指向头尾low，high，mid指向中间：
  如果mid所指的值大于等于low，说明mid处于第一段非递减序列，最小值还在后面，把low移到mid位置；
  如果mid所指的值大于等于high，说明mid处于第二段非递减序列，最小值在前面，把high移到mid位置；
  当high - low == 1时，说明刚好在旋转点位置，最小值就是high所指元素。
但是，如果有重复元素，当出现 low == high == mid 的情况时，就无法判断最小值位于哪一个区间，只能遍历搜索。（这边直接调用了min函数，可以自己实现一个遍历搜索函数）

时空复杂度：
- 时间复杂度 O(logn)
- 空间复杂度 O(1)

Test Cases：
- 输入为空数组，输入数组长度为1
- 输入数组未经过旋转
- 输入数组首尾相等，最小值在中间
- 有重复元素

⚠️
沟通是否有重复元素（题目意思是非递减序列，是会有重复元素）
'''
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        low, high = 0, len(rotateArray) - 1
        if rotateArray[low] < rotateArray[high]:
            return rotateArray[low]
        while high - low > 1:
            mid = low + (high - low) / 2
            if rotateArray[low] == rotateArray[high] and rotateArray[low] == rotateArray[mid]:
                return min(rotateArray[low:high+1])
            if rotateArray[mid] >= rotateArray[low]:
                low = mid
            elif rotateArray[mid] <= rotateArray[high]:
                high = mid
        return rotateArray[high]
