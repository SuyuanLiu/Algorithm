# -*- coding:UTF-8 -*-
'''
Question:
给出一个由0,1组成的网格，找出从原点走到特定点的最短路径长度。
网格中1表示可以走，0表示不可以走。走的方向上下左右四个方向。

Solution:
- BFS. 宽度优先搜索
- BFS在宽度上搜索，也就是第i步所能走的所有的点都要搜索；如果第一次被BFS遍历到，说明此时就是最短路径；
- 需要建立一个队列，存储每一轮遍历到的点；
- 还要对已经遍历过的点进行标记，比如置为-1等。（如果题目要求不可以改变原网格数据，需要最后进行还原） 

'''
class Solution:
    def findPath(self, grid, posx, posy, Q):
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        lr, lc = len(grid), len(grid[0])
        for i in range(4):
            curx, cury = posx + x[i], posy + y[i]
            if 0 <= curx < lr and 0 <= cury < lc and grid[curx][cury] == 1:
                Q.append((curx, cury))

        return Q


    def minPath(self, grid, tr, tc):
        if not grid:
            return 
        if tr == 0 and tc == 0:
            return 0
        
        Q = [(0,0)]
        path = 0
        while Q:
            for i in range(len(Q)):
                cur = Q.pop(0)
                grid[cur[0]][cur[1]] = -1
                if cur == (tr, tc):
                    return path 
                else:
                    Q = self.findPath(grid, cur[0], cur[1], Q)
            path += 1

        return -1
