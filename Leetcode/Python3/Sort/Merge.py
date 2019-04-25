# -*- coding:UTF-8 -*-
'''
Solution: 归并排序，时间复杂度O(nlogn),空间复杂度O(n);
- 思想就是，让数组左边独自有序，右边独自有序，然后合并左右两部分；
- 递归使得数组左右有序；
（归并就是每个单独的数，把他们两两相邻合并有序，然后再把这些小数组相邻的合并有序）
'''
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        return self.merge(left, right)
        
    
    def merge(self, A, B):
        C = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1 
        while i < len(A):
            C.append(A[i])
            i += 1 
        while j < len(B):
            C.append(B[j])
            j += 1 
        return C 
    
    def sortIntegers(self, A):
        # write your code here
        A = self.mergeSort(A)
        return A
        