'''
@lsy 2019.12.25

dfs
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    cnt += 1
        return cnt
                    
                    
    def isValid(self, i, j, grid):
        return (0 <= i < len(grid) and 0 <= j < len(grid[0]))

    def dfs(self, i, j, grid):
        grid[i][j] = ''
        
        pos_x = [0, 0, 1, -1]
        pos_y = [1, -1, 0, 0]
        for n in range(4):
            x, y = i + pos_x[n], j + pos_y[n]
            if self.isValid(x, y, grid) and grid[x][y] == '1':
                self.dfs(x, y, grid)