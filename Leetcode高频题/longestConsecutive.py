'''
@lsy 2019.11.27

Solution 1:
定义一个哈希表，存以当前数字为边界的长度。
读取数字，更新这个数字所在区间的两个边界的最大长度。中间的数值更新与否都可以。
读取一个数字 n, 去找它的左右两侧的数字 n-1, n+1 看是否在哈希表内。
'''
# Solution 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxLen, dic = 0, {}
        for n in nums:
            if n in dic.keys():
                continue
            
            is_left = n-1 in dic.keys()
            is_right = n+1 in dic.keys()
            
            left = dic[n-1] if is_left else 0
            right = dic[n+1] if is_right else 0
            
            dic[n] = left + right + 1
            dic[n-left] = dic[n+right] = dic[n]
            
            maxLen = max(maxLen, dic[n])
            
        return maxLen