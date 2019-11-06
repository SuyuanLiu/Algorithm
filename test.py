class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        import pdb; pdb.set_trace()
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            # left is sorted
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                
            # right is sorted    
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1
                
                
s = Solution()
nums = [3,1]
print(s.search(nums, 1))