# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n < 2:
            return n 
        n1, n2 = 1, 1
        res = 1
        for i in range(2, n)
            res = n1 + n2
            n1 = n2 
            n2 = res 
        return res

s = Solution()
print(s.Fibonacci(3))
