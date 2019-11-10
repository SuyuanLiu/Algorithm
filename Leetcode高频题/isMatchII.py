'''
@lsy 2019.11.10

自己写了个DP超时了。
在Discuss那边看了个解法，目前还不是很理解。
'''
class Solution:
    def isMatch(self, strr: str, pattern: str) -> bool:
        s, p, match, starIdx = 0, 0, 0, -1
        while s < len(strr):
            if p < len(pattern) and (strr[s] == pattern[p] or pattern[p] == '?'):
                s, p = s + 1, p + 1
            elif p < len(pattern) and pattern[p] == '*':
                starIdx = p
                match = s
                p += 1
            elif starIdx != -1:
                p = starIdx + 1
                match += 1
                s = match
            else:
                return False
            
        while p < len(pattern) and pattern[p] == '*':
            p += 1
        
        return p == len(pattern)