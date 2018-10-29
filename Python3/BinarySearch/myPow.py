# -*- coding:UTF-8 -*-
'''
Solution:
    - 利用二分思想；
    - 求x的n次方，首先把n转化为二进制形式；
    - 比如：10**75 = 10**1001011(二进制) = 10**(1000000) * 10**（1000） * 10**（10） * 10（1） 
                                        = 10**64  *  10**8  *  10**2  *  10**1
'''
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1
        newN = abs(n)
        while newN:
            if newN & 1:
                ans *= x
                
            x *= x
            newN >>= 1
        
        return ans if n>0 else 1/ans           
            
        