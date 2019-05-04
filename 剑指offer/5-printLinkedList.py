'''
解题思路：
Solution 1: 直接从头遍历一遍，最后倒着输出即可。
Solution 2: 利用栈，先进后出。（也可以用递归，但如果链表的结点很多，递归太深，会造成栈溢出的问题）

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)

Test Cases：
- 空链表
- 只有一个node，有多个node

⚠️
可以把链表指针全部翻转过来，然后遍历，实现从尾到头（感觉麻烦），但是这样改变了原本的数据，要跟面试官沟通是否能够改变原来的数据。

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1
class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        
        nums, node = [], listNode
        while node:
            nums.append(node.val)
            node = node.next
        return nums[::-1]


# Solution 2
class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        
        nums, stack = [], []
        node = listNode
        while node:
            stack.append(node)
            node = node.next 
        while stack:
            node = stack.pop()
            nums.append(node.val)
        return nums
