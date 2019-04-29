'''
Solution:
- 题意分析：N个皇后，不能放在同一行，同一列，或者同一对角线，返回所有可能放置的方法。
- 时间复杂度：O(n!)。由于不能在同一行，也不能在同一列，所以每行一个皇后，每列也分别一个，因此第一个皇后有N个位置可选，第二个皇后有N-1个位置，第三个有N-2个位置，因此时间复杂度是 O(n!)
- 分别定义draw，isValid，dfs函数。draw用来画皇后的位置，isValid判断当前位置放置皇后是否有效，dfs用来找到所有合适的放置方法。
- dfs，cols里面放的是前面几个皇后所在的列数，当cols中元素个数等于n时，说明N个皇后已经全部放置完成。在前面放置了x个皇后后，下一行皇后的位置从第0列到最后一列判断是否合适，注意每判断完一次，最后要pop最后一个元素
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.dfs([], n, [])
        
    def dfs(self, cols, n, res):
        if len(cols) == n:
            res.append(self.draw(cols))
            return res
        
        for i in range(n):
            if self.isValid(i, cols):
                cols.append(i)
                res = self.dfs(cols, n, res)
                cols.pop()
        return res
                
    
    def draw(self, cols):
        matrix = []
        for c in cols:
            s = ''
            for i in range(len(cols)):
                s = s + 'Q' if i == c else s + '.'
            matrix.append(s)
        return matrix
    
    def isValid(self, col, cols):
        n = len(cols)
        for i in range(n):
            if col == cols[i] or i + cols[i] == n + col or i - cols[i] == n - col:
                return False
        return True
