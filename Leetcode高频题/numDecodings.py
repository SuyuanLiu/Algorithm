'''
@lsy 2019.11.19

DP
要注意特殊情况的判断。
如果字符串无效，那么应该返回0！！！
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [0 for _ in range(len(s)+1)]
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0
        
        for i in range(len(s)-2, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
            else:
                continue
            if int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        
        return dp[0]


