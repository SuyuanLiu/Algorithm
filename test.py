class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        
        i = 0
        # import pdb; pdb.set_trace()
        while i < len(nums):
            if 0 < nums[i] <= len(nums):
                if nums[i] != i + 1:
                    idx = nums[i] - 1
                    nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    i += 1
            else:
                nums[i] = -1
                i += 1
        
        for i in range(len(nums)):
            if nums[i] == -1:
                return i + 1
        return len(nums) + 1

s = Solution()
nums = [3,4,-1,1]
print(s.firstMissingPositive(nums))
