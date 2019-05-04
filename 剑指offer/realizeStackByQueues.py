'''
解题思路：
栈：先进后出，队列：先进先出。
使用两个队列q1，q2，要保证任意时刻，两个队列中至少有一个为空。做push/pop操作时，只针对不空的那个进行操作；
  push：push到不为空的队列中去（如果两个都为空，随便push一个即可）
  pop：把不空的队列元素一个个转移到另一个队列中去，剩最后一个元素返回

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)

Test Cases：
- 空时pop，push
- pop中夹杂push
- pop一部分后全部push出来

⚠️
跟面试官沟通是否需要处理特殊情况：空时做pop操作。
'''
import queue


class Solution:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        
    def push(self, node):
        if not self.q1.empty():
            self.q1.put(node)
        else:
            self.q2.put(node)

    def pop(self):
        if not self.q1.empty():
            while self.q1.qsize() > 1:
                node = self.q1.get()
                self.q2.put(node)
            return self.q1.get()
        else:
            while self.q2.qsize() > 1:
                node = self.q2.get()
                self.q1.put(node)    
            return self.q2.get()    
