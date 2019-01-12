# -*- coding:UTF-8 -*-
'''
Solution:
- 生成小于n的所有平方项，除了直接使用乘法（如Solution 1 中），还可以使用加法（如Solution 2 中）

Solution 1: BFS
- BFS的两个重要步骤：
  1. 建一个队列：存储每一轮遍历的结点   2. 标记：对于已经遍历过的结点要做标记
- 这边就是如何把题目转化为图：图中的点由1-n整数构成了n个点，其中两点之差为平方项的话，那么两点之间有边；
  BFS应建立一个队列s来存储每一轮遍历到的数，对遍历过的数做标记（使用mark数组）

Solution 2: DP
- 建立一个长度为n+1的数组dp，dp[i]表示使用平方数组成数字i最少需要的个数。
- 那么dp[i]的值就是与i数值相差平方项的那些值中最小值加1，也就是：
  动态规划的公式：dp[i] = min(dp[i-squares]) + 1, 其中squares表示小于i的所有平方数。
'''
# Solution 2

class Solution:
    def geneSquare(self, n):
        squares = []
        square, diff = 1, 3
        while square <= n:
            squares.append(square)
            square += diff
            diff += 2
            
        return squares
        
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = self.geneSquare(n)
        dp = [0 for i in range(n+1)]
        
        for i in range(1, n+1):
            min_cnt = float('inf')
            for num in squares:
                if i >= num:
                    min_cnt = min(min_cnt, dp[i-num]+1)
            dp[i] = min_cnt
            
        return dp[n]


# Solution 2
class Solution:
    def geneSquare(self, n):
        squares = []
        cnt = 1
        while cnt * cnt <= n:
            squares.append(cnt*cnt)
            cnt += 1
            
        return squares    
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = self.geneSquare(n)
        mark = [False for i in range(n+1)]
        mark[n] = True
        s = [n]
        cnt = 1
        
        while s:
            for i in range(len(s)):
                cur_n = s.pop(0)
                for num in squares:
                    next_n = cur_n - num
                    if next_n == 0:
                        return cnt
                    if next_n > 0 and not mark[next_n]:
                        s.append(next_n)
                        mark[next_n] = True
            cnt += 1
        return n
                        
        
    
            