'''
@lsy 2019.11.26

双指针
注意：转换为小写islower()；判断是否为数字和字母isalnum()
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        s = s.lower()
        
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i] != s[j]:
                return False
            
            i, j = i + 1, j - 1
        
        return True
                