'''
Solution:
- 这题是求子集，使得子集的和为target，不同的地方在于同一个元素可以取无限次；
- 使用DFS，画出搜索树
- 先对数组排序，当取了当前的元素后，它的备选元素是从当前元素开始往后的所有元素（因为同一个元素可以取多次，所以备选元素要包括当前元素）注意这边是往后取，这样可以避免最后结果出现重复子集
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.dfs(candidates, [], [], target)
        
    
    def dfs(self, nums, path, res, target):
        if sum(path) == target:
            res.append([n for n in path])
            return res
        
        for i in range(len(nums)):
            tmp = target - sum(path)
            if nums[i] > tmp:
                break
            path.append(nums[i])
            res = self.dfs(nums[i:], path, res, target)
            path.pop()
        return res
