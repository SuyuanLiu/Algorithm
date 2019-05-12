'''
解题思路：
Solution 1:
这是一个大数题，要用字符串或者数组来解决，这边使用字符串。
初始化成一个长度为n，全部由'0'组成的字符串。
- 需要字符串的加1操作，注意遇到1999这种的加法；停止加1操作判断，如果下标i已经超出num范围，说明该停止加1计算。
  最开始想的是在printNmax这个主代码中判断 num != '9'*n，但书上写这个比较时间复杂度是O(n)的，在加1代码中判断时间复杂度为O(1)
- 打印字符串操作，注意前面的0不要打印出来

Solution 2:
看作是全排列，n个位置上0-9数字变换，全部排列一遍，使用递归。

Test Cases：
- n很大，n比较小，n为负数或0
'''
# Solution 1
class Solution():
    def __init__(self):
        self.nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def plusOne(self, num):
        tmp = num[-1]
        if tmp != '9':
            return num[:-1] + self.nums[int(tmp) + 1]
        
        i = -1
        while -i <= len(num) and num[i] == '9':
            i -= 1
        if -i > len(num):
            return ''
        num = num[:i] + self.nums[int(num[i]) + 1] + '0' * (abs(i)-1)
        return num

    def printNum(self, num):
        i = 0
        while num[i] == '0':
            i += 1
        print(num[i:])

    def printNmax(self, n):
        if n <= 0:
            return 
        num = '0' * n 
        num = self.plusOne(num)
        while num != '':
            self.printNum(num)
            num = self.plusOne(num)


# Solution 2
class Solution():
    def __init__(self):
        self.nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def printNum(self, num):
        i = 0
        while i < len(num) and num[i] == '0':
            i += 1
        if i == len(num):
            return 
        print(num[i:])

    def helper(self, num, idx):
        if idx == len(num):
            self.printNum(num)
            return 
        for i in range(10):
            num = num[:idx] + self.nums[i] + num[idx+1:]
            self.helper(num, idx+1)
    

    def printNmax(self, n):
        if n <= 0:
            return 
        num = '0' * n
        self.helper(num, 0)
