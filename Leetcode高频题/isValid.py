'''
@lsy 2019.10.30

这道题要求比较简单，要求匹配的符号中间不能插入其他单个符号。
使用栈，注意要随时判断是否栈空(for循环中的elif那边一开始忘记判断栈空)。
时间复杂度O(n)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 2 == 1:
            return False
        
        dic = {
            ')':'(', ']':'[', '}':'{'
        }
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            elif not stack or stack[-1] != dic[ch]:
                return False
            else:
                stack.pop()
            
        return not stack
