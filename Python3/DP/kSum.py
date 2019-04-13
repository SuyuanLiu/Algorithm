'''
Solution:
- 背包
- 建立一个三维矩阵，dp[i][j][p],表示从前i个数中取j个数，和为p的方法数有多少；
- 动态方程：dp[i][j][p] = dp[i-1][j][p]， if A[i-1] > p
                      = dp[i-1][j][p] + dp[i-1][j-1][p-A[i-1]]
- 初始化：dp[i][0][0] = 1
- ⚠️：在第二层循环，j in range(1, min(k+1,i+1))，从前i个数中取j个数，要保证j<=i;
'''
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        dp = [[[0 for p in range(target+1)] for j in range(k+1)] for i in range(len(A)+1)]
        dp[0][0][0] = 1 
        
        for i in range(1, len(A)+1):
            dp[i][0][0] = 1
            for j in range(1, min(k+1,i+1)):
                for p in range(1, target+1):
                    if A[i-1] > p:
                        dp[i][j][p] = dp[i-1][j][p]
                    else:
                        dp[i][j][p] = dp[i-1][j-1][p-A[i-1]] + dp[i-1][j][p]
        return dp[-1][-1][-1]
