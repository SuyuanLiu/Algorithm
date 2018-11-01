# -*- coding:UTF-8 -*-
'''
Solution:
参考：https://www.youtube.com/watch?v=LPFhl65R7ww
- 这道题是分治的思想，用到二分法，时间复杂度O(log(min(m,n)))
- 要找到中位数，就要对数组进行划分，中位数左右侧数组长度固定；

- 在nums1上进行二分查找，假设nums1的划分点是partition1，那么nums2的划分点是(m+n+1)//2-partition1
  nums1： a1, a2, | a3, a4, a5, a6                     ( | 表示分割点)
  nums2： b1, b2, b3, b4, b5, b6, | b7, b8, b9
  数组有序，已经满足 a2 < a3, b6 < b7;
  如果再满足： a2 < b7, b6 < a3, 那么分割点左侧所有的数值都小于分割点右侧的值，那么中位数就在 [a2, b6, a3, b7] 之间产生；
  如果 a2 > b7, 说明左边的数值太大，需要把nums1的分割点向左移；
  如果 a2 < b7, 说明左边的数值太小，需要把nums1的分割点向右移；

- 当m+n为奇数时，中位数为 (max(L1,L2)+min(R1,R2))/2， 否则max(L1,L2)。  （其中L1,R1,L2,R2分别为两分割线左右侧的值）
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)               # 在短的数组上进行二分查找
        if m == 0:
            return nums2[n//2] if n%2 else (nums2[n//2]+nums2[n//2-1])/2
        
        partition1 = m // 2
        halfLen = (m + n + 1) // 2
        
        while True:
            partition2 = halfLen - partition1
            
            L1 = -(float('inf')) if partition1 == 0 else nums1[partition1-1]
            R1 = float('inf') if partition1 == m else nums1[partition1]
            L2 = -(float('inf')) if partition2 == 0 else nums2[partition2-1]
            R2 = float('inf') if partition2 == n else nums2[partition2]            
        
            if L1 <= R2 and L2 <= R1:
                return max(L1,L2) if (m+n)%2 else (max(L1,L2)+min(R1,R2))/2
            elif L1 > R2:
                partition1 -= 1
            else:
                partition1 += 1