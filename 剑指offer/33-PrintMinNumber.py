'''
解题思路：
参考：https://www.nowcoder.com/questionTerminal/8fecd3f8ba334add803bf2a06af1b993
- 首先，这是一个大数问题，多个数字拼接起来可能会超过系统所能表示的最大值，所以要用字符串来表示
- 重新定义两个数字大小的定义：a, b, 如果 ab > ba，那么 a > b；否则 b > a
- 利用上述定义，对数组进行排序
- 最后把排好序的数组直接拼接起来即可
（如果是非python语言，比如C++，可以直接在sort那边调用重新定义的cmp函数）

Test Cases：
- 空数组
- 数组只有一个数字
- 数组有多个数字，有重复数字；有重复的数位

'''
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, nums):
        # write code here
        if not nums:
            return ''
        nums = list(map(str, nums))
        nums.sort(cmp = lambda x, y: cmp(x+y, y+x))
        # str.lstrip(s) 作用是，把str字符串前面是s的部分全部删掉，比如 '000324'.lstrip('0') --> '324'
        return "".join(nums).lstrip('0') or'0'
