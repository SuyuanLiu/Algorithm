'''
@lsy 2019.11.30

DP
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        wordDict = sorted(wordDict, key=lambda x: len(x))
        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    break
                if s[i - len(word) + 1:i + 1] == word and dp[i - len(word) +
                                                             1]:
                    dp[i + 1] = True
                    break

        return dp[-1]
