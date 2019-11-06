'''
@lsy 2019.11.6

二分搜索。
分为两种情况：
- nums[mid] >= nums[left], 说明mid左边有序，判断target是否在 left, mid之间即可； 
- nums[mid] < nums[right], 说明mid右边有序，判断target是否在 mid, right之间即可。
需要注意的是：
- nums[mid] >= nums[left],这边的等号不能去掉，否则不能通过只有两个元素的情况，比如[3,1],target=1
  这是因为mid=(left+right)//2,在数组长度为偶数时，下标取值偏向于左侧。
- 里面的判断等号也不要少
- while l <= r，等号

时间复杂度O(logn)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            # left is sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                
            # right is sorted    
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
                