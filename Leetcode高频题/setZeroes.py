'''
@lsy 2019.11.16

看不懂题解，也看不下去，下次再看吧。
照着高票Discuss的代码。
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isZeroCol, isZeroRow = False, False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isZeroCol = True
                break

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                isZeroRow = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if isZeroCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if isZeroRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
