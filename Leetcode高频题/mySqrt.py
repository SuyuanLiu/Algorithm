'''
@lsy 2019.11.15
二分搜索
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        start, end = 1, x
        
        while start <= end:
            mid = start + (end - start) // 2
            num = mid * mid
            if num == x:
                return mid 
            elif num > x:
                end = mid - 1
            elif (mid+1) * (mid+1) > x:
                return mid
            else:
                start = mid + 1
            
# Solution 2: Concise       
class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid > x:
                end = mid - 1
            elif (mid + 1) * (mid + 1) > x:
                return mid 
            else:
                start = mid + 1
                  