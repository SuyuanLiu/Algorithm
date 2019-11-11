'''
@lsy 2019.11.11

二分搜索。
注意：
在 n < 0 时，一开始写的是：
 n = -n
 x = 1 / x
这样会出现误差。
比如：34.00515，-3， 结果应为 0.0005， 计算结果为 0.0006
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n & 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n >> 1)
