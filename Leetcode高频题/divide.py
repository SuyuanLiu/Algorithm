'''
@lsy 219.11.1

使用减法。
- 使用sign来记录最终结果的符号。
- 注意使用了技巧，对被除数divisor进行翻倍扩大，这样可以加快计算，否则会Time Limit Exceeded.
- 最后return，因为python数值可能超过2^31，所以进行限制（不是很懂这个return）
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                quotient += i
                dividend -= tmp
                tmp <<= 1
                i <<= 1
        quotient = quotient if sign else -quotient
        return min(max(-2147483648, quotient), 2147483647)
            
            