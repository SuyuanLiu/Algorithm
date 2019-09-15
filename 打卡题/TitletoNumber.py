'''
@lsy 2019.9.15
找规律
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += pow(26, len(s)-i-1) * (ord(s[i]) - ord('A') + 1)
        return res
