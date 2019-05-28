'''
解题思路：
因为有重复的数字，所以要对字符串做一个排序。
使用递归，path为前面i个字符已经排列好的序列，在剩余的字符中依次选取每个字母作为第i+1个位置的字母，然后依次递归。
递归结束的条件是：s长度为1，直接把s放在path后，把对应的字符串append到res中。   
注意：会有重复字母，所以在for循环取字母时，遇到重复字母不必重复去取，直接跳过即可。

时空复杂度：(这个不太确定)
- 时间复杂度 O(n!)
- 空间复杂度 O(n!)

Test Cases：
- 空串
- 有重复字母的
- 没有重复字母的

'''
# -*- coding:utf-8 -*-
class Solution:
    def helper(self, s, path, res):
        if len(s) == 1:
            res.append(path+s)
            return res
        for i in range(len(s)):
            if i != 0 and s[i] == s[i-1]:
                continue
            tmp = path + s[i]
            res = self.helper(s[:i]+s[i+1:], tmp, res)
        return res
        
    def Permutation(self, s):
        # write code here
        if not s:
            return []
        tmp = list(s)
        tmp.sort()
        s = ''.join(tmp)
        return self.helper(s, '', [])
