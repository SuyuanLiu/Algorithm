'''
Solutio:
- DFS，画出搜索树，类似有重复元素的，找子集
- 这边注意，在搜索树的同一层，对于重复元素只取一次
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, start, path, res):
        if sum(path) == target:
            res.append([n for n in path])
            
        for i in range(start, len(nums)):
            tmp = target - sum(path)
            if nums[i] > tmp:
                break
            if i != start and nums[i] == nums[i-1]:   # deal with duplicates in the same level
                continue
            
            path.append(nums[i])
            self.dfs(nums, target, i+1, path, res)
            path.pop()
