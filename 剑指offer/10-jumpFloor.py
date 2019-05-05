'''
解题思路：
跟斐波那契数列是一个思路。（DP）
跳到第n个台阶的方法等于跳到n-1和n-2方法的和，f(n) = f(n-1) + f(n-2)。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- n = 0, 1, 2, ...

'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 3:
            return number
        n1, n2 = 1, 2
        res = 2
        for i in range(2, number):
            res = n1 + n2 
            n1 = n2
            n2 = res
        return res
