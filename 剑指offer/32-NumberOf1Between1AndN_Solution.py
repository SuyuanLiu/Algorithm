'''
解题思路：
Solution 1
遍历
- 对于数字n，进行 %10 操作，计算数字 n 中 1 的个数
- 遍历每个数字，把所有数字中 1 的个数进行加和
- 时间复杂度 O(nlogn), 空间复杂度 O(1)

----------------------------------------------
Solution 2
(暂时没看懂)牛客讨论区：https://www.nowcoder.com/questionTerminal/bd7f978302044eee894445e244c7eee6

----------------------------------------------
Test Cases：

⚠️
'''
# -*- coding:utf-8 -*-
# Solution 1
class Solution:
    def helper(self, n):
        cnt = 0
        while n:
            if n % 10 == 1:
                cnt += 1
            n //= 10
        return cnt
    
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        for i in range(1, n+1):
            res += self.helper(i)
        return res


# Solution 2
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        cnt, base = 0, 1
        while base <= n:
            high, low = n // base, n % base
            if high % 10 == 0:
                cnt += high / 10 * base
            elif high % 10 == 1:
                cnt += (high // 10 * base) + (low + 1)
            else:
                cnt += (high // 10 + 1) * base
            base *= 10
        return cnt 
