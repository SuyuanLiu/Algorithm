'''
@lsy 2019.10.21

Solution:
双指针。

使用字典dic来存储目前已经出现过的所有字符的最远的距离。
指针i，j。移动指针j，
- 若当前字符未在dic中出现，加入dic
- 若当前字符在dic中出现，判断当前字符之前出现的最远位置，如果在i,j之间，说明出现重复字符，需要将i指针移动到dic[s[j]] + 1
  更新当前字符出现的最远位置。

时间复杂度O(n)，空间复杂度O(n)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        if len(s) < 2:
            return len(s)
        
        dic, cnt = {}, 0
        i, j = 0, 0
        while j < len(s):
            c = s[j]
            if c in dic.keys() and i <= dic[c] < j:
                i = dic[c] + 1
                
            dic[c] = j
            j += 1
            cnt = max(cnt, j-i)
            
        return cnt
                
        
        