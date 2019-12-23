# class Solution:
#     def evalRPN(self, tokens):
#         stack = []
        
#         for n in tokens:
#             if n not in ['*', '/', '+', '-']:
#                 stack.append(self.str2int(n))
#             else:
#                 num1 = stack.pop()
#                 num2 = stack.pop()
#                 import pdb; pdb.set_trace()
#                 print(num2, num1, self.calculate(num2, num1, n))
                
#                 stack.append(self.calculate(num2, num1, n))
#         return stack.pop()
                
    
#     def calculate(self, num1, num2, op):
#         if op == '+':
#             return num1 + num2
#         if op == '-':
#             return num1 - num2
#         if op == '*':
#             return num1 * num2
#         if op == '/':
#             return num1 // num2
            
            
#     def str2int(self, s):
#         num = 0
#         for i, c in enumerate(s[::-1]):
#             if i == len(s) - 1 and c == '-':
#                 num = -num
#             else:
#                 num += int(c) * pow(10, i)
#         return num
            
# x = Solution()
# s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# print(x.evalRPN(s))

a = [3,30,34,5,9]
b = [str(n) for n in a]
print(b)
b.sort(reverse=True)
print(b)