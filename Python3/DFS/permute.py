# -*- coding:UTF-8 -*-
'''
Solution 1: DFS(BackTracking)
- 定义dfs函数，res存放最终结果，permutation前几位可能的结果；(即第一个数字可能的情况，前两个数字可能的情况等)

Solution 2: 
- 考虑的是把nums中的数字一个一个的插入到res中的path里面去；
- 比如nums=[1,2,3],一开始是把1插入到[]，变成[1]；然后是把2插入到[1],有[2,1], [1,2]两种；最后是把3插入到[2,1], [1,2]中，...
'''

# Solution 2
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        for n in nums:
            temp_res = []
            for path in res:
                for i in range(len(path)+1):
                    temp_res.append(path[:i]+[n]+path[i:])
            res = temp_res
        
        return res
        

# Solution 1
class Solution:
    def dfs(self, nums, res, permutation):
        if len(nums) == 1:
            res.append(permutation+nums)
        else:
            for i in range(len(nums)):
                res = self.dfs(nums[:i]+nums[i+1:], res, permutation+[nums[i]])
        return res
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        return self.dfs(nums, [], [])
        