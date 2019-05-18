'''
解题思路：
注意判断边界条件。每次从[i,i]位置开始打印一圈：横着👉，竖着👇，横着👈，竖着👆。

时空复杂度：
- 时间复杂度 O(m*n)
- 空间复杂度 O(m*n)

Test Cases：
- 数组为空
- 只有一个元素
- 只有一行/一列元素
- 行数 > 列数， 列数 > 行数

'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def helper(self, matrix, start, res):
        row, col = len(matrix), len(matrix[0])
        if start * 2  >= row or start * 2 >= col:
            return res
        
        i, j = start, start
        
        for j in range(start, col-start):
            res.append(matrix[i][j]) 

        for i in range(start+1, row-start):
            res.append(matrix[i][j])

        if j > start and i > start:
            while j > start:
                j -= 1
                res.append(matrix[i][j])

            while i > start + 1:
                i -= 1
                res.append(matrix[i][j])
                
        res = self.helper(matrix, start+1, res)
        return res
    
    def printMatrix(self, matrix):
        if not matrix:
            return 
        res = []
        return self.helper(matrix, 0, res)
