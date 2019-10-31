'''
@lsy 2019.10.31

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        
        all_combinations = []
        
        def helper(cur_path, left_parenthese_num, n):
            if left_parenthese_num == 0 and n == 0:
                all_combinations.append(cur_path)
            elif not cur_path:
                cur_path = '('
                helper(cur_path, 1, n-1)
            elif n < 1:    
                helper(cur_path + ')', left_parenthese_num - 1, n)
            elif left_parenthese_num == 0:
                cur_path += '('
                helper(cur_path, 1, n-1)
            else:
                helper(cur_path + '(', left_parenthese_num + 1, n-1)
                helper(cur_path + ')', left_parenthese_num - 1, n)
        
        helper('', 0, n)
        return all_combinations