'''
@lsy, 2019.10.19

Leetcode 1
Solution:
使用字典即可。注意不要使用一个数字超过两次。
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        dic = {}
        for i in range(len(nums)):
            
            
            tmp = target - nums[i]
            if tmp in dic:
                return [i, dic[tmp]]
                
            dic[nums[i]] = i
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return 
        
        dic = dict(zip(nums, [i for i in range(len(nums))]))
        for i, n in enumerate(nums):
            num = target - n
            if num in dic.keys() and dic[num] != i:
                return [i, dic[num]]        