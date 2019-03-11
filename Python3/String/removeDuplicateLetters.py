# -*- coding:UTF-8 -*-
'''
Solution:
- 用一个字典保存每个字母出现的次数，stack存放最终结果。
- 当字母c在stack中，不做操作，直接把cnt中对应的出现次数减1；
  当字母c不在stack中时，判断stack是否为空，为空直接加入；
     stack不为空时，对字母c和stack最后一个字母进行比较，
     如果该字母的字母序比c大并且cnt对应的值大于0（说明后面还有这个字母），那么就删掉这个字母；
     因为要保留不重复的最小的字母。
'''
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # import collections
        # cnt = collections.Counter(s)
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        
        stack = []
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and cnt[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            cnt[c] -= 1
                
        return ''.join(stack)
