'''
@lsy 2019.10.30

使用字典存储数字与对应的字母。
下面代码第一个是我自己写的代码，第二个是根据discuss修改的：
- 修改dic里面的值，不必使用list
- 变量命名，使用all_combinations, current_combinations更容易理解
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'], 
            '4' : ['g', 'h', 'i'], 
            '5' : ['j', 'k', 'l'], 
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        res = []
        for ch in digits:
            if not res:
                res = dic[ch]
            else:
                tmp = []
                for s in res:
                    for c in dic[ch]:
                        tmp.append(s+c)
                res = tmp
        return res

# code modified
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2' : 'abc',
            '3' : 'def', 
            '4' : 'ghi', 
            '5' : 'jkl', 
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        all_combinations = []
        for ch in digits:
            if not all_combinations:
                all_combinations = dic[ch]
            else:
                current_combinations = []
                for s in all_combinations:
                    for c in dic[ch]:
                        current_combinations.append(s+c)
                all_combinations = current_combinations
        return all_combinations