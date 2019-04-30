'''
Solution:
- 找到所有的结果，DFS，尝试画搜索树看一下
- 类似subset题，这边假设在不同的位置进行切割，前面已经切割的，要判断是否是回文串，是的话继续，不是的话就停止🤚
- 搜索树的叶子结点是最终的结果
- ⚠️注意：同样的，res.append([c for c in path])，这边如果直接append(path)，会出错
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        return self.dfs(s, 0, [], [])
        
        
    def dfs(self, s, start, res, path):
        if start >= len(s):
            res.append([c for c in path])
            return res
        
        for i in range(start, len(s)):
            if not self.isPalindrome(s[start : i+1]):
                continue
            path.append(s[start : i+1])
            res = self.dfs(s, i+1, res, path)
            path.pop()
        return res
        
    
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
