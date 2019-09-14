'''
@lsy  2019.9.14
题目的follow up是只遍历一次，不用额外空间，在这个基础上去思考。
同时，题目给定的board一定是有效的。
思路：
其实是计算有几片连通域，因为board一定有效，所以X若连通的话，要么是行，要么是列。
因此在遇到X，判断右方或者下方是否为X，如果是X，继续，如果不是，此时cnt加1.
就是相当于对这片连通域，只在遍历到最后一个点的时候，才进行加1操作。
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i + 1 < len(board) and board[i+1][j] == 'X') or \
                       (j + 1 < len(board[0]) and board[i][j+1] == 'X'):
                        continue
                    else:
                        cnt += 1
  
        return cnt
        
        
