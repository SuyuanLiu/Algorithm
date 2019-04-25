'''
Solution:
- DP,一般设置的大小要比sequence长度大一个，要考虑s1的第0个字符与s2的其他字符公共子序列；
- dp[i][j]表示的是第一个串的前i个字符与第二个串的前j个字符的最长公共子序列；
- 动态方程：dp[i][j] = dp[i-1][j-1] + 1 ,           if A[i-1] == B[j-1]
                   = max(dp[i-1][j], dp[i][j-1]),  else
- 初始化第0行和第0列，都是0；
- 注意：因为dp的长度比实际子串长度大1，所以判断A[i-1] == B[j-1]，这边要减1，否则out of index.
'''
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        
        n, m = len(A), len(B)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[-1][-1]
