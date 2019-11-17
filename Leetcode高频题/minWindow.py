'''
@lsy 2019.11.17

不会，照着discuss写的，下次看。
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        need = collections.Counter(t)
        missing = len(t)
        start, end = 0, 0
        i = 0
        for j, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            
            need[c] -= 1
            
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1
                missing += 1
                if end == 0 or j - i < end - start:
                    start, end = i, j
                
                i += 1
        return s[start:end]
            
            