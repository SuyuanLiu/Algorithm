'''
Solution:
- 使用DFS，模拟搜索树
- 时间复杂度 O(n!),这种的测试集数据不会很大，一般n<=20

Solution 2:
通用型DFS
'''
# Solution 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, [])
        return res
        
    def dfs(self, nums, res, path):
        if len(path) == len(nums):
            res.append([c for c in path])
            return 
        
        for n in nums:
            if n not in path:
                path.append(n)
                self.dfs(nums, res, path)
                path.pop()
        
            

# Solution 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        return self.permuteHelper(nums, [])
        
    def permuteHelper(self, nums, path):
        res = []
        if len(nums) < 2:
            res = [p + nums for p in path] if path else [nums]
            return res
        
        for i in range(len(nums)):
            path_ = [p + [nums[i]] for p in path] if path else [[nums[i]]]
            res += self.permuteHelper(nums[:i] + nums[i+1:], path_)
        
        return res
