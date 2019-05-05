# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        low, high = 0, len(rotateArray) - 1
        if rotateArray[low] < rotateArray[high]:
            return rotateArray[low]
        while high - low > 1:
            mid = low + (high - low) // 2
            if rotateArray[low] == rotateArray[high]:
                return min(rotateArray[low:high+1])
            if rotateArray[mid] > rotateArray[low]:
                low = mid
            elif rotateArray[mid] < rotateArray[high]:
                high = mid
        return rotateArray[high]

s = Solution()
print(s.minNumberInRotateArray([3,4,5,1,2]))
