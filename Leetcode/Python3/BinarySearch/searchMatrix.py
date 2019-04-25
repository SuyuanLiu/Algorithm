# -*- coding:UTF-8 -*-
'''
Solution:
- 二分思想
- 从矩阵的右上角的点开始比较，如果target比它大，说明target在下面的行(i += 1)，小则在前面的列(j -= 1)

Solution 2:
- 两个二分,时间复杂度O(logn + logm = log(n*m))
- 先用第一个二分去找到target在哪一行（对第一列数找到最后一个小于等于target的数）；
- 然后在那一行，用二分去找target
（这个方法比较麻烦，注意二分出来之后一定要判断start和end，因为如果数组只有一个数，就不会进入while循环）

Solution 3:
- 只用一个二分法，时间复杂度O(log(n*m))
- 把它看成一个一维数组（因为下一行的数值全部大于上一行的值）

'''
class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if not matrix:
            return False
        
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        
        while 0 <= i < row and 0 <= j < col:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
                
        return False

# Solution 2
class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if not matrix or len(matrix[0]) == 0:
            return False
                
        row, col = len(matrix), len(matrix[0])
        
        start, end = 0, row - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target < matrix[mid][0]:
                end = mid
            else:
                start = mid        
        if matrix[end][0] <= target:
            tmp = end
        else:
            tmp = start
            
        start, end = 0, col - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target == matrix[tmp][mid]:
                return True
            elif target > matrix[tmp][mid]:
                start = mid
            else:
                end = mid
        if target == matrix[tmp][start] or target == matrix[tmp][end]:
            return True
        
        return False

# Solution 3
class Solution:
    def toCordinate(self, num, col):
        return num // col, num % col
    
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if not matrix or not matrix[0]:
            return False
        
        row, col = len(matrix), len(matrix[0])
        start, end = 0, row * col - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            i, j = self.toCordinate(mid, col)
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                start = mid
            else:
                end = mid
                
        i, j = self.toCordinate(start, col)
        if target == matrix[i][j]:
            return True
        i, j = self.toCordinate(end, col)
        if target == matrix[i][j]:
            return True
        
        return False
