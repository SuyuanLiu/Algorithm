'''
@lsy 2019.11.7

使用set。
遍历数组，把数字以 num in column i, num in row j, num in block x-y 的形式存入到set里面去。
每个小block里面是否重复的判断是用 i//3 and j//3 进行判断。
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                
                c_column = c + 'in column %d'%i
                c_row = c + 'in row %d'%j
                c_block = c + 'in block %d-%d'%(i//3, j//3)
                
                if c_column in visited or c_row in visited or c_block in visited:
                    return False
                else:
                    visited.update([c_column, c_row, c_block])
        
        return True
                