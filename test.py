class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        import collections
        queue = collections.deque()
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if (i in [0, row-1] or j in [0, col-1]) and board[i][j] == 'O':
                    queue.append([i, j])
                    
        import pdb;pdb.set_trace()
        pos = [[0,1], [0,-1],[1,0],[-1,0]]    
        while queue:
            x, y = queue.popleft()
            board[x][y] = 'A'
            for p in pos:
                new_x, new_y = x + p[0], y + p[1]
                if 0 <= new_x < row and 0 <= new_y < col and board[new_x][new_y] == 'O':
                    queue.append([new_x, new_y])
                    
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            
s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)