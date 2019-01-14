# -*- coding:UTF-8 -*-
'''
Solution: DFS

Solution 1:
- 借鉴https://github.com/SuyuanLiu/Leetcode/blob/master/Python3/DFS/maxAreaOfIsland.py这一题代码风格；
- 思路类似[Max Area of Island](https://leetcode.com/problems/max-area-of-island/)，把连通区域的数值全部换成其他值，即可；

Solution 2：
- 参考Discuss里面的代码，这个代码比较精简；
'''
# Solution 2
class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = ''
        
        pos_i = [0, 0, 1, -1]
        pos_j = [1, -1, 0, 0]
        for n in range(4):
            self.dfs(grid, i+pos_i[n], j+pos_j[n])
    
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

# Solution 1
class Solution:
    def isArea(self, grid, i , j):
        r, c = len(grid), len(grid[0])
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != '1':
            return False
        else:
            grid[i][j] = ''
            return True
        
    def dfs(self, grid, i, j):
        pos_i = [0, 0, 1, -1]
        pos_j = [1, -1, 0, 0]
         
        stack = [(i, j)]
        cnt = 0
        while stack:
            cur_i, cur_j = stack.pop()
            if self.isArea(grid, cur_i, cur_j):
                cnt += 1
                for n in range(4):
                    tmp_i, tmp_j = cur_i + pos_i[n], cur_j + pos_j[n]
                    stack.append((tmp_i, tmp_j))
        return cnt > 0
        

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(grid, i, j):
                    cnt += 1
        
        return cnt