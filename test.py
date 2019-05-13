# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return array
        
        i = 0
        while i < len(array):
            while i < len(array) and array[i] & 0x1 == 1:
                i += 1
            j = i 
            while j < len(array) and array[j] & 0x1 == 0:
                j += 1
            if j >= len(array):
                break
            for k in range(j, i, -1):
                array[k], array[k-1] = array[k-1], array[k]
            i = j
        return array

s = Solution()
nums = [3,5,2,4,7,6,1,9,8]
print(s.reOrderArray(nums))
