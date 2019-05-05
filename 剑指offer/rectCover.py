'''
解题思路：
斐波那契变形，f(n) = f(n-1) + f(n-2)

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- n = 0, 1, 2, ...
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 4:
            return number
        n1, n2 = 1, 2
        for i in range(2, number):
            tmp = n1 + n2
            n1 = n2
            n2 = tmp
        return tmp
