# -*- coding:UTF-8 -*-
'''
Solution:
- 二分思想
- 从矩阵的右上角的点开始比较，如果target比它大，说明target在下面的行(i += 1)，小则在前面的列(j -= 1)
- 或者从左下角的点开始找。

Follow up:
Question: https://www.lintcode.com/problem/search-a-2d-matrix-ii/description
如果数组中有重复的值，找出target出现了几次；

Solution: 
- 时间复杂度：O(m+n)
- 从右上角开始，如果target比它大，就往下走；小就往左走；相等则向左下角走；(相当于每次去掉一行或者一列，时间复杂度可以从这里考虑)
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


# Follow up Solution
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
            
        row, col = len(matrix), len(matrix[0])
        cnt = 0
        i, j = 0, col - 1 
        while 0 <= i < row and 0 <= j < col:
            if target == matrix[i][j]:
                cnt += 1 
                i, j = i + 1, j - 1 
            elif target > matrix[i][j]:
                i += 1 
            else:
                j -= 1 
        return cnt 
