'''
题目：
https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=1

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
        res = 2å
        for i in range(2, number):
            res = n1 + n2 
            n1 = n2
            n2 = res
        return res
