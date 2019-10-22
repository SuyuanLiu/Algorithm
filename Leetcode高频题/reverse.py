'''
@lsy 2019.10.22

Solution:
直接对10取余，然后乘起来加起来即可。
注意：
python的负数在整除和取余操作上跟其他语言不一样
- -124 // 10 = -13
- -124 % 10 = 6 (???)
overflow的判断是针对reverse后的数值进行判断的
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x != 0:
            tmp = x % 10
            res = res * 10 + tmp
            x = int(x / 10)
        
        if res > 0x7fffffff:
            return 0
        else:
            return res * sign