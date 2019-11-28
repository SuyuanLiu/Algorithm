'''
@lsy 2019.11.28

dfs
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        res = []
        def dfs(idx, path):
            if idx >= len(s):
                res.append([c for c in path])
                return 
            
            for i in range(idx, len(s)):
                if not self.isPalindrome(s[idx:i+1]):
                    continue
                dfs(i+1, path + [ s[idx:i+1] ])
                # path.append(s[idx:i+1])
                # dfs(i+1, path)
                # path.pop()
        
        dfs(0, [])
        return res
    
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True