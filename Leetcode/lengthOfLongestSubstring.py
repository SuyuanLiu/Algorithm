'''
解题思路：
- 双指针
- 分别指向当前不重复子串的头，尾
- 用字典记录当前出现过的所有字符的最后的一个位置
- 在当前i，j范围内，判断第j个字符出现的位置是否在i,j之间，
  是的话，说明有重复字符，直接把i指针移到这个字符的下一个位置；
  不在i，j之间的话，当前子串长度加1，把新的字符添加到字典中；

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)

⚠️
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        i, j = 0, 1
        res, tmp = 1, 1
        dic = {s[0]:0}
        
        while j < len(s):
            if s[j] in dic and dic[s[j]] >= i:
                i = dic[s[j]] + 1
                dic[s[j]] = j
                tmp = j - i + 1
            else:
                tmp += 1
                res = max(res, tmp)
                dic[s[j]] = j
            j += 1
        return res
