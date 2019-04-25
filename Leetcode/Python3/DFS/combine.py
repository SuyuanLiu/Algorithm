# -*- coding:UTF-8 -*-
'''
Solution: BackTracking

Solution 1:
- 排列组合，先确定第一个数，再依次确定后面的数
- 定义dfs，nstart是从i+1开始的

Solution 2: TODO
'''

# Solution 1
class Solution:
    def dfs(self, n, k, nstart, res, path):
        if k == 1:
            for i in range(nstart, n+1):
                res.append(path+[i])
        else:
            for i in range(nstart, n-k+2):
                res = self.dfs(n, k-1, i+1, res, path+[i])
                
        return res
    
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.dfs(n, k, 1, [], [])
        
        
            