class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], 0, res)
        return res
        
        
    def dfs(self, nums, subset, start, res):
        res.append([c for c in subset])
        # import pdb; pdb.set_trace()
        
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, i+1, res)
            subset.pop()
            
            
s = Solution()
nums = [1,2,3]
print(s.subsets(nums))
