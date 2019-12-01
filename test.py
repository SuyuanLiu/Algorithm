class Solution:
    def wordBreak(self, s, wordDict):
        if not s:
            return True
        if not wordDict:
            return False

        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        wordDict = sorted(wordDict, key=lambda x: len(x))

        # import pdb
        # pdb.set_trace()

        for i in range(len(s)):
            if i < len(wordDict[0]) - 1:
                continue
            for word in wordDict:
                if i < len(word) - 1:
                    break
                # print(s[i - len(word) + 1:i + 1])
                if s[i - len(word) + 1:i + 1] == word and dp[i - len(word) +
                                                             1]:
                    dp[i + 1] = True
                    break

        return dp[-1]


x = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
# print(x.wordBreak(s, wordDict))
print(s.startswith('le'))
