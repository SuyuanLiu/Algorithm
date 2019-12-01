'''
@lsy 2019.12.1

使用哈希表。
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memory):
        if not s:
            return []
        if s in memory:
            return memory[s]
        
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resOfRest = self.helper(s[len(word):], wordDict, memory)
                for item in resOfRest:
                    item = word + ' ' + item
                    res.append(item)
        memory[s] = res
        
        return res
            