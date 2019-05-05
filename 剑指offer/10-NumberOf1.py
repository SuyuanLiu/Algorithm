'''
解题思路：
1. 可以对 n 与 1 做与操作，看最后一位是否为 1，然后把 n 右移 1 位。
   但是，⚠️，负数的话，最高位是符号位为1，右移之后在前面补1，这个做法会导致死循环。
2. 转换思路，对 1 做右移操作；
   要注意的是，在python中取整数没有精度限制，在其他语言中整数是32位，所以 while 结束的条件设置为小于0xffffffff；
   在其他语言中，结束条件为 num == 0。
3. 如果一个数字 n 不为 0，那么里面一定至少有一个 1。
   假设最后一位是1，那么 n-1 的最后一位变为0，其他位不变，
   假设最右边的1不是最后一位，那么 n-1 之后，它的1那位变为0，后面其他位全部变为1，之前的不受影响；
   因此，如果做 n & (n-1) 操作的话，最右边的1的后面就全部变为0。那么n中有几个1，就能做几次这样的操作。
   ⚠️python整数无限进度，所以负数前面相当于有无限个1，要做一下 n & 0xffffffff 操作。

Test Cases：
- n = 0, 1, 负数， 0x7fffffff, 0xffffffff, 0x80000000

'''
# -*- coding:utf-8 -*-
        
# Solution 2
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt, num = 0, 1
        while num <= 0xffffffff:
            if n & num:
                cnt += 1
            num <<= 1
        return cnt 

# Solution 3
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            cnt += 1
            n = (n-1) & n 
        return cnt
