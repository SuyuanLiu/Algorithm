'''
解题思路：
f(n) = f(n-1) + f(n-2)，递归存在重复计算，使用非递归的方法，记录f(n-1)，f(n-2)的值，直接计算。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- n = 0, 1, 2, ...

⚠️
沟通第一个元素是从0还是1开始，n=0时输出什么
'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n < 2:
            return n 
        n1, n2 = 1, 1
        res = 1
        for i in range(2, n):
            res = n1 + n2
            n1 = n2 
            n2 = res 
        return res
