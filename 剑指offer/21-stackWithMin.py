'''
解题思路：
本题的关键在于如何保存最小值的实现。
- 如果直接使用一个变量来保存最小值，那么当当前的最小值被弹出栈，此时栈的最小值为次小值，此时无法O(1)时间找到次小值；
- 考虑额外使用一个栈minS存储最小值信息。minS大小与stack大小一致，minS第i位存储的是，stack前i个元素中的最小值。
    比如在开始时压入5，此时最小值是5，在minS中压入最小值5. stack=[5], minS=[5]
    压入2，此时最小值是2，在minS中压入最小值2.           stack=[5,2], minS=[5,2]
    压入4，此时最小值依然是2，在minS中压入最小值2.        stack=[5,2,4], minS=[5,2,2]
    压入3，此时最小值依然是2，在minS中压入最小值2.        stack=[5,2,4,3], minS=[5,2,2,2]
    压入1，此时最小值是1，在minS中压入最小值1.           stack=[5,2,4,3,1], minS=[5,2,2,2,1]
在做弹出操作时，同时也要对minS做弹出。栈中最小值就是minS的栈顶元素。

时空复杂度：
- 时间复杂度 O(1)
- 空间复杂度 O(n)

Test Cases：
- 新压入元素比之前的最小值小/大
- 弹出元素是最小值/不是最小值

⚠️
沟通空栈时pop操作，min操作该返回什么
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minV = float('inf')
        self.minS = []
        
    def push(self, node):
        self.stack.append(node)
        if node < self.minV:
            self.minV = node
        self.minS.append(self.minV)
        
    def pop(self):
        if not self.stack:
            return 
        self.minS.pop()
        return self.stack.pop()
    
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    
    def min(self):
        return self.minS[-1]
