'''
@lsy 2019.11.1

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        len_hay, len_need = len(haystack), len(needle)
        if len_hay < len_need:
            return -1
        
        for i in range(len_hay - len_need + 1):
            if haystack[i : i+len_need] == needle:
                return i
            
        return -1
            
