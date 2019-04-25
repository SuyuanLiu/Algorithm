'''
Solution:
- DP, two sequence
- 特殊情况：如果 s1，s2 长度和与 s3 不等的话，直接return False
- 设置dp[n+1][m+1], dp[i][j] 表示 s1 的前 i 个字符与 s2 的前 j 个字符能否构成 s3 的前 i+j 个字符；
- 动态方程：dp[i][j] = dp[i-1][j], if s1[i-1] == s3[i+j-1]
                   = dp[i][j-1], if s2[j-1] == s3[i+j-1] and dp[i][j] == False
    如果 s1[i-1] == s3[i+j-1]，那么 dp[i][j] 的值就看能否构成 s3 的前 i+j-1 个字符；
    又因为 s1 的第 i 个字符与 s3 的第 i+j 个字符相等，就是要看 s1 的前 i-1 个字符 + s2 的前 j 个字符 ?= s3 的前 i+j-1 个字符，也就是dp[i-1][j]；
    第二行的方程，and dp[i][j] == False，是为了防止出现 s1[i-1] == s2[j-1] == s3[i+j-1]，dp[i][j]先被赋True，后被赋False的情况出现；
    （这边不知道会不会有这种情况）
- 结果：dp[-1][-1]
'''  
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        
        dp = [[False for j in range(m+1)] for i in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if dp[i-1][0] == False:
                break
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
                
        for j in range(1, m+1):
            if dp[0][j-1] == False:
                break
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
                
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if s2[j-1] == s3[i+j-1] and dp[i][j] == False:
                    dp[i][j] = dp[i][j-1]
                
        return dp[-1][-1]
