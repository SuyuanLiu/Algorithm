'''
解题思路：
- 没说数组是排好序的
- 使用字典
（总是做错这道题）

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        dic = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in dic and dic[tmp] != i:
                return [i, dic[tmp]]
