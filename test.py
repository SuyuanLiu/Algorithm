class Solution:
    def isValidSudoku(self, board):
        from collections import defaultdict
        dic = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    dic[board[i][j]].append((i,j))

        

        for num in dic.keys():
            positions = dic[num]
            print(positions)
            import pdb; pdb.set_trace()
            pos_x, pos_y = [], []
            for pos in positions:
                i, j = pos[0], pos[1]
                print(i,j)
                print(pos_x, pos_y)
                import pdb; pdb.set_trace()
                if i in pos_x or j in pos_y or (i // 3 in pos_x and j // 3 in pos_y):
                    return False
                else:
                    pos_x.append(i)
                    pos_y.append(j)
        return True

s = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(board))