# -*- coding:UTF-8 -*-
'''
Solution:
- 双指针，使用flag标记是否已经出现两次；
'''
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 3:
            return len(nums)
        
        flag, i = 0, 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                if flag == 0:
                    flag = 1
                    i += 1
                    nums[i] = nums[j]
                else:
                    continue
            else:
                i += 1
                nums[i] = nums[j]
                flag = 0
                
        return i + 1
