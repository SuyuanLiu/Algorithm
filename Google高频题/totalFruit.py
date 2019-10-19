'''
@lsy, 2019.10.19

Leetcode 904
题目相当于是，找最长连续子串，满足这个子串中的数字不超过两种。

Solution
双指针。
定义两个指针i，j。移动指针j，直到出现第三种水果。然后将移动指针i，直到移除最左侧类型的水果。
定义字典，存放对应fruit type的水果数。当len(dic) > 2时，说明超过两种水果，此时需要移动指针i。
每移动一次指针i，对应的 dic[tree[i]] 要减1，直到出现 dic[tree[i]] == 0，说明此时指针i，已经移除了一种水果了。然后在dic中删除这种类型。
在每次循环时，都去计算res即可。

时间复杂度O(n)，空间复杂度O(1).
'''
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        
        res = 1
        i, j = 0, 0
        dic = {}
        
        while j < len(tree):
            dic[tree[j]] = 1 if tree[j] not in dic.keys() else dic[tree[j]] + 1

            while len(dic) > 2:
                dic[tree[i]] -= 1
                if dic[tree[i]] == 0:
                    del dic[tree[i]]    
                i += 1
                    
            j += 1
            res = max(res, j - i)
            
        return res
            