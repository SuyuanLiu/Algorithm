'''
@lsy 2019.12.6

题目意思是：
    找到第一个运算符，前面两个数字进行运算，得出结果放在这个位置；
    然后继续寻找下一个运算符，进行运算
Solution：
    栈
注意:
    题目要求除法向0取整，所以应该用int来做。
    python可以：四舍五入，向0取整，向下取整，向上取整
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for n in tokens:
            if n not in ['*', '/', '+', '-']:
                stack.append(self.str2int(n))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(self.calculate(num2, num1, n))
        return stack.pop()
                
    
    def calculate(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        if op == '*':
            return num1 * num2
        if op == '/':
            return int(num1 / num2)
            
            
    def str2int(self, s):
        num = 0
        for i, c in enumerate(s[::-1]):
            if i == len(s) - 1 and c == '-':
                num = -num
            else:
                num += int(c) * pow(10, i)
        return num
            