'''
@lsy 2019.11.29

异或
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        res = 0
        for n in nums:
            res ^= n
            
        return res