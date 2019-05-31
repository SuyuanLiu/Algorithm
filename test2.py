# -*- coding:utf-8 -*-
class Solution:
    def isUngly(self, num):
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
        
    def GetUglyNumber_Solution(self, index):
        # write code here
        cnt, num = 1, 1
        while cnt < index:
            num += 1
            if self.isUngly(num):
                cnt += 1
        return num

s = Solution()
print(s.GetUglyNumber_Solution(3))
