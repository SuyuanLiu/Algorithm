'''
@lsy 2019.12.20

分为整数部分和小数部分。
- 整数：直接用整除来获取整数部分
- 小数：用字典来存储当前余数以及对应结果的长度。若当前余数在字典中出现，说明小数开始出现循环。

注意：
- 符号问题
- 除数为0
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        res = ''
        if (numerator > 0) ^ (denominator > 0):
            res += '-'
            
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)
        
        remainder = numerator % denominator
        if remainder == 0:
            return res
        
        res += '.'
        dic = {remainder: len(res)}
        while remainder != 0:
            remainder *= 10
            res += str(remainder // denominator)
            remainder %= denominator
            
            if remainder in dic.keys():
                idx = dic[remainder]
                res = res[:idx] + '(' + res[idx:] + ')'
                return res
            
            dic[remainder] = len(res)
            
        return res
            