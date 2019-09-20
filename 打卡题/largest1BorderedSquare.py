'''
@lsy  2019.9.20

从方形的右下角去看，去看这个点向上有几个1，向左有几个1；
然后再分别看右上角向左有几个1，看左下角向上有几个1.
维护两个矩阵，top，left，分别表示当前点(i,j)向上，向左有几个1.

视频讲解参考：https://www.youtube.com/watch?v=tXrCgWR7maQ
'''
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        top = [[0 for j in range(col)] for i in range(row)]
        left = [[0 for j in range(col)] for i in range(row)]
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0 :
                    top[i][j] = top[i-1][j] + 1 if i > 0 else 1
                    left[i][j] = left[i][j-1] + 1 if j > 0 else 1
                
    
        for a in range(min(row, col), 0, -1):
            for i in range(row-1, a-2, -1):
                for j in range(col-1, a-2, -1):
                    if top[i][j] >= a and left[i][j] >= a and left[i-a+1][j] >= a and top[i][j-a+1] >= a:
                        return a*a
        return 0
