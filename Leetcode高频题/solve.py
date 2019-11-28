'''
@lsy 2019.11.28
使用队列。
现在 board 四周找到 O，顺着这个 O 找出所有与之相连的 O，把他们都变成 A。
最后遍历 board，把那些 S 变成 O，把之前的 O 变成 X 即可。
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        queue = collections.deque()
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if (i in [0, row-1] or j in [0, col-1]) and board[i][j] == 'O':
                    queue.append([i, j])
                    
            
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
            