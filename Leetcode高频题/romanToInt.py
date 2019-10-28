'''
@lsy 2019.10.28

使用字典存储字符与对应的数值。
判断字符串当前位置数值是否小于下一个位置，是的话，减去当前位置对应数值。
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        num = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
                num = num - dic[s[i]] + dic[s[i+1]]
                i += 2
            else:
                num += dic[s[i]]
                i += 1
        return num
