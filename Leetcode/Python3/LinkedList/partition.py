# -*- coding:UTF-8 -*-
'''
Solution:
- 设置一个dummy node
- 设置一个lessNode，用来记录当前小于x的区域
- 用cur去遍历list，同时记录pre。遇到小于x的，pre直接指向cur的next，lessNode指向cur即可；
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        lessNode = dummy
        pre, cur = dummy, head
        while cur:
            if cur.val < x:
                if pre == lessNode:
                    lessNode = lessNode.next
                    tmp = cur.next
                    pre = cur
                    cur = tmp
                else:
                    pre.next = cur.next
                    tmp = lessNode.next
                    lessNode.next = cur
                    cur.next = tmp
                    
                    lessNode = lessNode.next
                    cur = pre.next
            else:
                tmp = cur.next
                pre = cur
                cur = tmp
                
        return dummy.next
