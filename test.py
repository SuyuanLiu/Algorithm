class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip(' ')
        if not str:
            return 0
        
        import pdb;pdb.set_trace()

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
        for i in range(len(validS)-1, 0, -1):
            num += pow(10, base) * int(validS[i])
            base += 1
            if num > 0x7fffffff:
                return pow(2, 31) - 1 if validS[0] != '-' else -pow(2, 31)
            
        if validS[0] in ['+', '-']:
            return num if validS[0] == '+' else -num
        
        num += pow(10, base) * int(validS[0])
        return num

s = Solution()
print(s.myAtoi("2147483648"))