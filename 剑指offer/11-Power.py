'''
解题思路：
要注意各种问题：
- exponent，指数小于0的情况
- base，底数为0的情况，要跟面试官沟通是返回0还是返回1.
- 由于base是float型，不能直接用 == 判断两个数是否相等，要用 <= 1e-10 这种去判断。
时间复杂度O(n)

优化：
a^x = a^(x/2) * a^(x/2), if x % 2 == 0
      a^(x/2) * a^(x/2) * a, if x % 2 == 1

- 用递归去计算
- 使用与操作代替 %，判断指数是奇数还是偶数，提高计算速度
- 对exponent做右移，代替除法，计算速度更快
- 时间复杂度O(logn)

Test Cases：
- base = 0，正常值
- exponent：0， +， -

'''
# -*- coding:utf-8 -*-
# Solution 1
class Solution:
    def Power(self, base, exponent):
        if abs(base) <= 1e-10:
            return 0
        res = 1
        flag = 1
        if exponent < 0:
            exponent = - exponent
            flag = 0
        for i in range(exponent):
            res *= base
        return res if flag == 1 else 1/res

# Solution 2
class Solution:
    def powerWithUnsigned(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.powerWithUnsigned(base, exponent >> 1)
        res *= res
        if exponent & 0x1 == 1:
            res *= base
        return res
        
    def Power(self, base, exponent):
        if abs(base) <= 1e-10:
            return 0
        if exponent < 0:
            return 1/self.powerWithUnsigned(base, -exponent)
        else:
            return self.powerWithUnsigned(base, exponent)
