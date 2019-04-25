# -*- coding:UTF-8 -*-
'''
Solution: DFS, Union find

Solution 1: DFS
- 思路类似[Friend Circles](https://leetcode.com/problems/friend-circles/)
- 遍历数组，如果M[i][j] == 1, 把第i行，第j列所有为1的元素都变为-1，这样就把所有的朋友关系都给遍历并且标记了；



'''


# Solution 1
class Solution:
    def dfs(self, M, i, j):
        if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]) or M[i][j] != 1:
            return 
        M[i][j] = -1
        
        for n in range(len(M)):
            self.dfs(M, n, j)
        for n in range(len(M[0])):
            self.dfs(M, i, n)

    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        cnt = 0
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    self.dfs(M, i, j)
                    cnt += 1
        
        return cnt
        