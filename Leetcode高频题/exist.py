'''
@lsy 2019.11.18

DFS.
对board中的每一个点去做dfs。
dfs停止的条件是：当前搜索长度等于word长度。
对于不可重复使用：可以使用额外空间记录状态，或者对遍历过的字符标记为'*'，在遍历完成后再变为原来的字母。
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
                
        return False
        
        
    def dfs(self, board, word, idx, i, j):
        if idx == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[idx] != board[i][j]:
            return False
        
        char = board[i][j]
        board[i][j] = '*'
        
        res = self.dfs(board, word, idx+1, i+1, j) or self.dfs(board, word, idx+1, i-1, j) or self.dfs(board, word, idx+1, i, j+1) or self.dfs(board, word, idx+1, i, j-1)
        
        board[i][j] = char
        
        return res
