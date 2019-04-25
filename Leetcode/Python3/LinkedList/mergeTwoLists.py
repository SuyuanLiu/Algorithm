# -*- coding:UTF-8 -*-
'''
Solution 1:
- 把两个lsit合并到一个新的listnode里面去，但这样会开辟额外的空间；

Solution 2：
- 不使用额外空间
- 下面使用cur指向当前已排好序的最后一位
'''
# Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:  return l2
        if not l2:  return l1

        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
            
        return dummy.next
            

# Solution 1
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:  return l2
        if not l2:  return l1
        
        dummy = ListNode(0)
        cur = dummy
        p, q = l1, l2
        while p and q:
            if p.val < q.val:
                cur.next = ListNode(p.val)
                p = p.next
            else:
                cur.next = ListNode(q.val)
                q = q.next
            cur = cur.next
        
        if p:
            cur.next = p
        if q:
            cur.next = q
            
        return dummy.next
