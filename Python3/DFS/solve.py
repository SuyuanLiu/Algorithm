'''
Solution 1: DFS
- 对四个边界进行查找，如果有'O',把与它相关联的'O'全部找出来，标记为'S'；
- 然后再把其他的'O'换成'X'，最后再把'S'换成'O'；

Solution 2: BFS
- 对四个边界查找，把全部放进队列里面；
- 对队列中的元素遍历，把他们变成'S'，它的四周中如果有'O'，则把坐标加入队列；
- 最后对整个board遍历，如果遇到'S'则变成'O'，如果是'O'则变成'X'；
'''
# Solution 1
class Solution:
    def findO(self, board, i, j):
        board[i][j] = 'S'
        row, col = len(board), len(board[0])
        pos_i = [1, -1, 0, 0]
        pos_j = [0, 0, 1, -1]
        for n in range(4):
            t_i, t_j = i + pos_i[n], j + pos_j[n]
            if 0 <= t_i < row and 0 <= t_j < col and board[t_i][t_j] == 'O':
                self.findO(board, t_i, t_j)
        
    
    def change(self, board, target, replacement):
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == target:
                    board[i][j] = replacement
            
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 1 or len(board[0]) == 1:
            return 
        
        row, col = len(board), len(board[0])
        for i in [0, row-1]:
            for j in range(col):
                if board[i][j] == 'O':
                    self.findO(board, i, j)
                    
        for i in range(row):
            for j in [0, col-1]:
                if board[i][j] == 'O':
                    self.findO(board, i, j)
                    
        self.change(board, 'O', 'X')
        self.change(board, 'S', 'O')