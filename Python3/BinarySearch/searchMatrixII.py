# -*- coding:UTF-8 -*-
'''
Solution:
- 二分思想
- 从矩阵的右上角的点开始比较，如果target比它大，说明target在下面的行(i += 1)，小则在前面的列(j -= 1)
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while 0 <= i < row and 0 <= j < col:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False
