'''
@lsy 2019.11.7

使用递归。
注意循环里面初值设置以及位置。
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            last_str = self.countAndSay(n-1)
            res = ''
            pre_c, i, cnt = '', 0, 0
            while i < len(last_str):
                pre_c = last_str[i]
                i, cnt = i + 1, 1
                while i < len(last_str) and last_str[i] == pre_c:
                    i += 1
                    cnt += 1
                res += '%d'%cnt + pre_c
                
            return res