# -*- coding:UTF-8 -*-
'''
Solution:
- 二分法
- 看到first，就想到二分法；

'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
                
        if isBadVersion(start):
            return start
        return end
