# -*- coding:UTF-8 -*-
'''
Question：
有一个容量为W的背包。现在有N个物品，编号为0...n-1，其中没一件物品体积为w(i)，价值为v(i)。
问可以向这个背包中放物品的最大总价值。

Solution:DP

Solution 1：时间复杂度O(NW), 空间复杂度O(NW)
- 定义一个二维数组dp[N+1][W+1],其中dp[i][j]表示前i件体积不超过j的最大价值。假设第i见物品体积价值为w,v，那么
  dp[i][j] = dp[i-1][j]          ，不放入第i件物品
           = dp[i-1][j-w] + v    ，放入第i件物品
注意要判断j，w的大小。

Solution 2：时间复杂度O(NW), 空间复杂度O(2W) 
- 由上面的公式，可以看出，dp[i][j]只与第i-1行的相关，所以可以进行优化，dp只保留两行；

Solution 3：时间复杂度O(NW), 空间复杂度O(W)
- 使用一维数组来维护dp,从上面公式看出dp[j] = max(dp[j], dp[j-w]+v)，这边的dp[j]可以表示dp[i][j]和dp[i-1][j];
- 注意这边对dp[j]进行更新的时候，要从(W+1,0)去更新，因为上一轮的dp[j]是针对dp[i-1][j],本轮针对的是dp[i][j],
  而 dp[i][j] = ...dp[i-1][j-w]...,如果j从1开始增大的话，那么dp[i-1][j-w]先被更新为dp[i][j-w]，当去更新dp[i][j]是用到的dp[j-w]实际就是dp[i][j-w]了；
  因此j要从(W+1,0)去更新，倒着更新，防止dp[i-1][j-w]被dp[i][j-w]覆盖；
'''

# Solution 3
class Solution():
    def knapsack(self, W, N, weights, values):
        dp = [0 for i in range(W+1)]
        for i in range(N):
            w = weights[i]
            v = values[i]
            for j in range(W, 0, -1):
                if j >= w:
                    dp[j] = max(dp[j], dp[j-w]+v)

        return dp[W]


# Solution 2
class Solution():
    def knapsack(self, W, N, weights, values):
        dp = [[0 for i in range(W+1)] for j in range(2)]
        for i in range(1, N+1):
            w = weights[i-1]
            v = values[i-1]
            for j in range(1, W+1):
                if j >= w:
                    dp[i%2][j] = max(dp[(i-1)%2][j], dp[(i-1)%2][j-w]+v)
                else:
                    dp[i%2][j] = dp[(i-1)%2][j]
        return dp[N%2][W]


# Solution 1
class Solution():
    def knapsack(self, W, N, weights, values):
        dp = [[0 for i in range(W+1)] for j in range(N+1)]
        for i in range(1, N+1):
            w = weights[i-1]
            v = values[i-1]
            for j in range(1, W+1):
                if j >= w:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][W]
