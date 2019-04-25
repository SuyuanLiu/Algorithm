# -*- coding:UTF-8 -*-
'''
Solution 1: DFS(Backtracking)
- 定义dfs函数，res保存结果，letters保存当前遍历到的结果；

Solution 2:
- 参考Discuss答案；
- 遍历digits，用temp_res存放前i个数字对应的所有组合；
'''
# Solution 2
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        dic = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for digit in digits:
            temp_res = []
            for c in dic[int(digit)]:
                temp_res += [s + c for s in res]
            res = temp_res
            
        return res
                
        

# Solution 1
class Solution:
    def dfs(self, digits, res, letters):
        dic = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        num = int(digits[0])
        if len(digits) == 1:
            for i in range(len(dic[num])):
                res.append(letters+dic[num][i])
        else:
            for i in range(len(dic[num])):
                res = self.dfs(digits[1:], res, letters+dic[num][i])
                
        return res
        

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        return self.dfs(digits, [], '')
        
        
        