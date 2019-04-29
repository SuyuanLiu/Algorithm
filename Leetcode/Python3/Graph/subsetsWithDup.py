'''
Solution:
- 题目要求找到所有的子集，想到dfs，可以画一下搜索树，树的每一个结点都是一个子集
- 这边先对数组排序，便于处理重复元素，遇到重复元素时，在当前这一轮（即同一个树高的层上，取了第一个，后面的就不再取了）
- 时间复杂度 O(2^n),对于每个元素都有选择和不选择两种情况
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return
        
        nums.sort()
        self.dfs(nums, [], 0, res)
        return res
        
    def dfs(self, nums, subset, start, res):
        res.append([n for n in subset])
        
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, subset, i+1, res)
            subset.pop()
        return res
