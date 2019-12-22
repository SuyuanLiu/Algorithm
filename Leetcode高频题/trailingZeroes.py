'''
@lsy 2019.12.22

参考解释：https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages
0个个数，就是要看这个数字里面有几个10，而10 = 5 * 2，也就是看这个阶乘中有多少个因数为5.
- 2,5中，个数比较少的那个数字决定了最终结果中有几个10.
- 而在阶乘中，2的数量远丰富于5，比如每两个数中就至少有一个2的因数。
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        baseNum = 5
        
        while n >= baseNum:
            cnt += n // baseNum
            baseNum *= 5
            
        return cnt