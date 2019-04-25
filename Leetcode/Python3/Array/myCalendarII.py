# -*- coding:UTF-8 -*-
'''
Solution 1: 暴力解法，时间复杂度O(n^2)
- 建两个数组，一个存放订阅的时间booktime，一个存放重叠的时间overlap;
- 对新的时间段，首先检查是否与overlap有重叠部分；没有重叠的话，在booktime中一一比较，如果有重叠，把重叠的部分加入overlap；

Solution 2：

'''

# Solution 1
class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.booktime = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for os, oe in self.overlap:
            if start < oe and end > os:
                return False
        for bs, be in self.booktime:
            if start < be and end > bs:
                self.overlap.append((max(bs,start), min(be,end)))
        self.booktime.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)