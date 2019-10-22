'''
@lsy 2019.10.22

Solution 1: DP
设置二维dp数组，dp[i][j]表示以i开头j结尾的字符串是否为回文串；
公式:   dp[i][j] = dp[i+1][j-1] if s[i] == s[j]
初始化: dp[i][i] = True
        dp[i-1][i] = True if s[i-1] == s[i]
结果:   True中长度最长的那个子串
注意点：
        因为 dp[i][j] = dp[i+1][j-1]，所以循环时i是递减循环，j是递增循环
        初始化可以合并到for循环中，加入判断即可
        在for循环中，使用maxLen来标记当前最长长度，用来判断是否更新子串结果
时间复杂度O(n^2)，空间复杂度O(n^2)

Solution 2:
从一个点出发，向两边出发寻找最长回文子串。
分别考虑回文串长度为奇数和偶数情况。
时间复杂度O(n^2)，空间复杂度O(1)
'''
# Solution 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        
        maxLen, res = 0, ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res = s[i:j+1] if j-i+1 > maxLen else res
                    maxLen = max(maxLen, j-i+1)
        
        return res
        
# Solution 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i+1), res, key=len)
        return res
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1 : r]