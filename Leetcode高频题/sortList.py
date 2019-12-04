'''
@lsy 2019.12.04

归并排序。
- 使用双指针，找到链表中点，将链表分为左右两部分
- 对左右两部分分别进行排序
- 然后对排好序的两部分合并
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        right = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(right)
        return self.mergeTwoSortedList(left, right)
    
    
    def mergeTwoSortedList(self, left, right):
        dummyNode = ListNode(-1)
        cur = dummyNode
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
            
        if left:
            cur.next = left
        if right:
            cur.next = right
            
        return dummyNode.next