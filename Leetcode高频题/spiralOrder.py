'''
@lsy 2019.11.12

使用四个坐标方向来辅助移动。
用direction记录当前移动方向：右，下，左，上
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        res = []
        
        compass = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, col = 0, -1
        direction = 0
        step = [len(matrix[0]), len(matrix) - 1]
        
        while step[direction % 2]:
            for i in range(step[direction%2]):
                row += compass[direction][0]
                col += compass[direction][1]
                res.append(matrix[row][col])
            step[direction % 2] -= 1
            direction = (direction + 1) % 4
            
        return res