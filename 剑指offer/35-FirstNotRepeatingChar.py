'''
解题思路：
- 遍历字符串，用字典存储每个字符出现的次数
- 遍历字典，把所有出现次数为1的字符加入到candidate
- 遍历字符串，如果当前字符在candidate里面，就说明当前字符就是第一个出现的字符
（可以优化，不必遍历字典）
（字典存储字符出现次数完毕之后，直接遍历第二遍字符串，每遇见一个字符就去看这个字符出现的次数）

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(1)，由于字符数最多是256个，是固定的大小，所以可以看作是O(1)

Test Cases：
- 空串
- 没有只出现一次的字符
- 存在只出现一次的字符
- 所有字符都只出现一次

'''
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        dic = {}
        for c in s:
            if c not in dic.keys():
                dic[c] = 1
            else:
                dic[c] += 1
        candidate = []
        for key in dic.keys():
            if dic[key] == 1:
                candidate.append(key)
        
        if not candidate:
            return -1
        else:
            for i in range(len(s)):
                if s[i] in candidate:
                    return i 
