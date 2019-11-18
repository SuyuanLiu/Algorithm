'''
@lsy 2019.11.18

不知道我用的方法是不是backtracking。

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        def helper(path, nums_cur):
            if not nums_cur:
                return
            for i, n in enumerate(nums_cur):
                tmp_path = path + [n]
                res.append(tmp_path)
                helper(tmp_path, nums_cur[i+1:])
                
        helper([], nums)
        return res