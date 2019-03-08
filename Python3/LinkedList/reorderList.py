# -*- coding:UTF-8 -*-
'''
Solution:
- 三个步骤：
    找到链表中点；（注意这边如果链表长度为偶数，返回第一个中点）
    把链表后半部分翻转；
    把两个链表交叉连接；
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findMiddle(self, head):
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        
        mid = self.findMiddle(head)
        right = self.reverseList(mid.next)
        mid.next = None
        
        l1, l2 = head, right
        while l1 and l2:
            tmp1 = l1.next
            l1.next = l2
            l1 = tmp1
            
            tmp2 = l2.next
            l2.next = l1
            l2 = tmp2
