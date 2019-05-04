'''
解题思路：
栈：先进后出，队列：先进先出。
使用两个栈A，B。当push时，对A进行操作；pop时，对B进行操作。
  push：A一直push即可，在最后面加入元素
  pop：把A中元素依次pop出来，并放入B中，此时B中是A的逆序，直接pop即可实现题目要求的先进先出。
做法：push直接在A中append；pop时把A中元素依次倒入到B，然后pop，再把B中元素全部倒回到A。
优化（Solution 2）：在B不为空的时候，pop时可以直接从B中pop。此时对pop，push代码做相应的修改。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)

Test Cases：
- 空时pop，push
- pop中夹杂push
- pop一部分后全部push出来

⚠️
跟面试官沟通是否需要处理特殊情况：空时做pop处理。
'''
# Solution 1
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
        
    def push(self, node):
        self.stackA.append(node)
        
    def pop(self):
        while self.stackA:
            node = self.stackA.pop()
            self.stackB.append(node)
        res = self.stackB.pop()
        while self.stackB:
            node = self.stackB.pop()
            self.stackA.append(node)
        return res

# Solution 2
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
        
    def push(self, node):
        while self.stackB:
            tmp = self.stackB.pop()
            self.stackA.append(tmp)
        self.stackA.append(node)
        
    def pop(self):
        if not self.stackB:
            while self.stackA:
                tmp = self.stackA.pop()
                self.stackB.append(tmp)
        node = self.stackB.pop()
        return node
