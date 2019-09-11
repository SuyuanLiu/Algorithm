'''
@lsy  2019.9.11
动态规划。
- 设置数组dp[n+1]，dp[i]表示以第i个字符结尾，能否由wordDict表示。
- 动态方程：dp[i] = (dp[i-len(word1)] and word1 == s[i-len(word1)-1:i+1]) or
                  (dp[i-len(word2)] and word2 == s[i-len(word2)-1:i+1]) or ...
  就是把wordDict里面所有的word都判断一遍；
- 初始化：在s前面加一个空符，dp[0] = True
- 结果：dp[-1]

时间复杂度O(mn)，空间复杂度O(n)
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = sorted(wordDict, key = lambda x: len(x))
        
        s = ' ' + s
        dp = [False for i in range(len(s))]
        dp[0] = True
        
        for i in range(1, len(s)):
            for word in wordDict:
                if len(word) > i:
                    break
                if s[i-len(word)+1:i+1] == word:
                    dp[i] = dp[i] or dp[i-len(word)]
        return dp[-1]
            
        