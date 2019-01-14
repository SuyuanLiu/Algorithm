# -*- coding:UTF-8 -*-
'''
Solution: DFS
- DFS就是从当前点，遍历到下一个结点，再到下一个，但是最后还能回到最开始的点，这就需要递归，栈；
- 使用DFS有两点：
  使用一个递归栈，存储遍历的结点；  对已经遍历过的结点做标记；

Solution 1:
- 递归：最大连通域等于当前面积加上临边的面积
- 对已经遍历过的点，对其置为-1，如果要求不可以变动原grid，记得最后要恢复数据；

Solution 2：
- 迭代：使用一个栈，保存当前点以及其临边，计算面积
- 对已经遍历过的点，对其置为-1，如果要求不可以变动原grid，记得最后要恢复数据；
'''

# Solution 2
class Solution:
    def isArea(self, grid, i, j):
        r, c = len(grid), len(grid[0])
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != 1:
            return False
        else:
            grid[i][j] = -1
            return True
        
    
    def dfs(self, grid, i, j):
        pos_i = [1, -1, 0, 0]
        pos_j = [0, 0, 1, -1]
        
        stack = [(i, j)]
        area = 0
        while stack:
            cur_i, cur_j = stack.pop()
            if self.isArea(grid, cur_i, cur_j):
                area += 1
                for n in range(4):
                    tmp_i = cur_i + pos_i[n]
                    tmp_j = cur_j + pos_j[n]
                    stack.append((tmp_i, tmp_j))
        return area

        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, self.dfs(grid, i, j))
                
        return area



# Solution 1
class Solution:
    def dfs(self, grid, i, j):
        r, c = len(grid), len(grid[0])
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != 1:
            return 0
        
        area = 1
        pos_i = [1, -1, 0, 0]
        pos_j = [0, 0, 1, -1]
        grid[i][j] = -1
        
        for n in range(4):
            area += self.dfs(grid, i+pos_i[n], j+pos_j[n])
        
        return area
        

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, self.dfs(grid, i, j))
                
        return area
        