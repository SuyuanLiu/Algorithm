# -*- coding:UTF-8 -*-
'''
Solution:
- 利用二分思想，时间复杂度 O(logN)；
- 除法的思想就是看被除数dividend中含有几个除数divisor，可以转化为减法；
- 每次相减时，除数都要扩大两倍；
'''

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1
        
        quotient = quotient if sign else-quotient
        
        return min(max(-2147483648, quotient), 2147483647)     # 防止溢出???不知道是不是还有别的方法，不是很懂，还要再思考；