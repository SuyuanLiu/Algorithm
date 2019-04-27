# class Solution:
#     def permute(self, nums):
#         if len(nums) < 2:
#             return [nums]
#         return self.helper(nums, [])
        
#     def helper(self, nums, path):
#         res = []
#         if len(nums) < 3:
#             if path == []:
#                 res = [nums, nums[::-1]]
#             else:
#                 for p in path:
#                     res.append(p + nums)
#                     res.append(p + nums[::-1])
#             return res
        
#         for i in range(len(nums)):
#             path_ = [p + [nums[i]] for p in path] if path else [[nums[i]]]
#             res += self.helper(nums[:i] + nums[i+1:], path_)
            
#         return res

class Solution:
    def permute(self, nums):
        if not nums:
            return []
        return self.permuteHelper(nums, [])
        
    def permuteHelper(self, nums, path):
        res = []
        if len(nums) < 2:
            res = [p + nums for p in path] if path else [nums]
            return res
        
        for i in range(len(nums)):
            # import pdb; pdb.set_trace()
            path_ = [p + [nums[i]] for p in path] if path else [[nums[i]]]
            res += self.permuteHelper(nums[:i] + nums[i+1:], path_)
        
        return res

s = Solution()
nums = [1,2,3]
print(s.permute(nums))
