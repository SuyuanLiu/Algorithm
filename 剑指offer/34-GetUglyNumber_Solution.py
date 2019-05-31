'''
解题思路：
Solution 1:
- 用一个函数计算num是否是丑数
- 遍历每个数字，直到直到第index个丑数
- 但是时间复杂度很高(没通过牛客第测试)

Solution 2:
- 想办法生成丑数，而不是判断每个数是不是丑数
- 用空间换时间，把丑数按顺序保存在数组中
- 假设当前数组中已经有n个丑数，那么下一个丑数一定是前面所有丑数中乘 2，3，5中较小的一个
- 用三个指针分别指向乘2，3，5之后刚好比最后一个丑数大的位置

Test Cases：
- 0, 1
- 2，3，4，5，6
- 很大的数，1500
'''
# -*- coding:utf-8 -*-
# Solution 1
class Solution:
    def isUngly(self, num):
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
        
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index

        cnt, num = 1, 1
        uglyNum = [1]
        while cnt < index:
            num += 1
            if self.isUngly(num, uglyNum):
                cnt += 1
        return num

# Solution 2
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        
        uglyNum = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(index - 1):
            num = min(uglyNum[t2] * 2, uglyNum[t3] * 3, uglyNum[t5] * 5)
            uglyNum.append(num)
            if num == uglyNum[t2] * 2:
                t2 += 1
            if num == uglyNum[t3] * 3:
                t3 += 1
            if num == uglyNum[t5] * 5:
                t5 += 1
        return uglyNum[-1]
