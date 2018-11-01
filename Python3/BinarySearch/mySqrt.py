class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 0, x
               
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            else:
                if (mid+1) * (mid+1) > x:
                    return mid
                start = mid + 1
                