# -*- coding:UTF-8 -*-
'''
Solution:
- 双指针
- 从两个数组的后面比较，比较大的放到nums1的末尾；
- 如果从小的开始比较，nums1里面有比较多的数字移动，时间复杂度比较高；

Follow up:
Question: 把两个有序数组合并到一个数组，开辟额外空间。如果m，n不是一个数量级的，一个非常非常大，一个很小，该怎样优化？
Solution：使用二分法，把对大数组进行二分，把小数组里面的数一个一个插入到大数组里面，用的是数组整体拷贝，整体拷贝比一个一个从数组里面拿数要快。
（这个问题可能对C++比较有意义，python不清楚....)
'''
class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        p = len(nums1) - 1 
        while i >=0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
            
        while j >= 0:
            nums1[p] = nums2[j]
            j, p = j - 1, p - 1
