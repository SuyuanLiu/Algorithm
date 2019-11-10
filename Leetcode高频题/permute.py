'''
@lsy 2019.11.10

分不清backtracking与DFS的区别。
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        
        def helper(path, nums_left):
            if not nums_left:
                res.append(path)
                return 
                
            for i in range(len(nums_left)):
                helper(path + [nums_left[i]], nums_left[:i]+nums_left[i+1:])
            
        helper([], nums)
        return res 
    
    
        