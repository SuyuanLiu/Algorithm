'''
Solution:
- DP, 类似longest common subsequence
- dp[i][j]表示以i，j结尾的最长公共子串；（注意是要以i，j结尾的！）
- 动态方程: dp[i][j] = dp[i-1][j-1] + 1 ， if A[i-1] == B[j-1]
                    = 0 ,                 else
- 注意由于dp长度比字符串长度要大1，所以判断时A[i-1] == B[j-1]，要减1，否则out of index
- 最后返回数组中最大的值；

（应该可以做空间上的优化）
'''
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0
            
        n, m = len(A), len(B)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        maxLen = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    dp[i][j] = 0
                maxLen = max(maxLen, dp[i][j])
        return maxLen
