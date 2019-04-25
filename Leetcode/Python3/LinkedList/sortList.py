# -*- coding:UTF-8 -*-
'''
Solution 
- 题目要求nlogn，额外空间O(1)
- 排序的话，时间为nlogn的有堆排序，快排，归并排序；
    堆排序要建立一个堆，有额外的空间；
    快排不使用额外空间，但是时间复杂度不是严格的nlogn；
    归并排序，时间严格的nlogn，对于链表不会使用额外空间
- 这里要分为三个步骤：找中点，合并两个有序list，划分；
    找中点：这边slow，fast不在同一个位置出发，这样当有偶数个时，返回第一个中点；
- sortList中，要注意判断特殊情况

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
    
    def mergeTwoLists(self, l1, l2):
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
            
        if l1:  cur.next = l1
        if l2:  cur.next = l2
            
        return dummy.next

    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        mid = self.findMiddle(head)
        if not mid.next:
            return self.sortList(head)
        
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.mergeTwoLists(left, right)
