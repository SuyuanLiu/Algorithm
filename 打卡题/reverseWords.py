'''
@lsy  2019.9.28
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])  
