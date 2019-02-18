# -*- coding:UTF-8 -*-
'''
Solution:
- 三步翻转法的思想
- 注意这边直接用split()
- 如果用split(' ')，对于s = ' ', 或者s = '   '之类的情况无法解决；
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        s1 = ' '.join(_s[::-1] for _s in s.split())
        return s1
