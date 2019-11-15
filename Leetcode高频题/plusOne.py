'''
@lsy 2019.11.15
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + carry
            digits[i], carry = num % 10, num // 10
            if carry == 0:
                return digits
            
        if carry != 0 :
            digits.insert(0, 1)
        
        return digits