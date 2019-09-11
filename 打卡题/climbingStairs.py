'''
@lsy    2019.9.11
斐波那契数列。
动态规划，f(n) = f(n-1) + f(n-2)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        f1, f2 = 1, 2
        for i in range(n-2):
            tmp_f = f1 + f2
            f1 = f2
            f2 = tmp_f
        return f2
