'''
Solution:
- DP
- dp[i][j]表示第一个字符串的前i个变成第二个字符串的前j个最少需要多少步；
- 状态方程：dp[i][j] = dp[i-1][j-1]， if word1[i-1] == word2[j-1]
                   = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1， else
- 初始化：第一行，也就是要把s1的前i个变为空串需要多少步，也就是i步；
- 结果：dp[-1][-1]
- 依旧注意，dp数组长度比字符串长度大1
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) if not word2 else len(word2)
        
        n, m = len(word1), len(word2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
