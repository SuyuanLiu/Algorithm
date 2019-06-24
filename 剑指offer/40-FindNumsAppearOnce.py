'''
解题思路：
注意这道题是：数组中有两个数字只出现一次，其他数字都出现了两次。
如果是数组中只有一个数字出现一次，其他出现两次，直接全部异或，最后都结果就是要找的数字。 
本题思路：
- 依旧是利用异或原理，相同为1，不同为0
- 将数组中所有数字异或一遍，得到数值num，因为有两个只出现一次的值，所以num一定不为0
- 找到num二进制表示中第一个为1的idx，这一位为1，说明两个数字在这一位一定不同，一个为1，一个为0
- 利用以上特点，对数组中的数进行分组，把idx位为1的分到一组，idx为0的分到另一组
- 上面分组方式一定保证了两个只出现一次的数字分在两个组，同时相同的数字也在一个组
- 对分组之后的再利用“只有一个数字出现一次”的方法，全部异或

注意：具体写代码时，分组与异或可以放在一起进行。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)

Test Cases：
- 数组中没有重复数字
- 数组中有多对重复数字
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def firstBitOf1(self, num):
        idx = 0
        while num & 1 == 0:
            idx += 1
            num >>= 1
        return idx
    
    def isBit1(self, num, idx):
        num >>= idx
        return num & 1 == 1
    
    def FindNumsAppearOnce(self, array):
        num = array[0]
        for i in range(1, len(array)):
            num ^= array[i]
            
        idx = self.firstBitOf1(num)
        
        res1, res2 = 0, 0
        for n in array:
            if self.isBit1(n, idx):
                res1 ^= n
            else:
                res2 ^= n
        return [res1, res2]
