'''
@lsy 2019.10.22

Solution:
注意各种特殊条件的判断。
'''
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip(' ')
        if not str:
            return 0
        
        digitals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if str[0] not in ['+', '-'] + digitals:
            return 0
        
        validS = str[0]
        for i in range(1, len(str)):
            if str[i] in digitals:
                validS += str[i]
            else:
                break
                
        num = 0
        base = 0
        sign = 1
        for i in range(len(validS)-1, 0, -1):
            num += pow(10, base) * int(validS[i])
            base += 1

        if validS[0] in ['+', '-']:
            sign = -1 if validS[0] == '-' else 1
        else:
            num += pow(10, base) * int(validS[0])
        
        if num > 0x7fffffff:
            return pow(2, 31) - 1 if sign == 1 else -pow(2, 31) 
        else:
            return num * sign
            

        