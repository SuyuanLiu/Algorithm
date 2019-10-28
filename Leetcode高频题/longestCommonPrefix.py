'''
@lsy 2019.10.28

Solution 1: 两层循环嵌套：
对字符串长度进行排序，然后对每个字符串去判断当前字符是否相同。
时间复杂度O(n*min(len(s)))

Solution 2:
参考discuss的朋友的方法。
'''
# Solution 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = ''
        strs.sort(key=lambda x: len(x))
        for i in range(len(strs[0])):
            tmp = ''
            for s in strs:
                if not tmp:
                    tmp = s[i]
                elif s[i] == tmp:
                    continue
                else:
                    return prefix
            prefix += tmp
        return prefix
            
# Solution 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
       
        shortestS = min(strs, key=len)
        for i, c in enumerate(shortestS):
            for s in strs:
                if s[i] != c:
                    return shortestS[:i]
        return shortestS

