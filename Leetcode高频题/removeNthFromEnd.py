'''
@lsy 2019.10.30

双指针
使用dummyNode指向head指针，以应对head被删除的情况。
设置快慢指针，都从dummyNode开始。快指针先走n步，然后两指针一起走，直到快指针走到最后。
注意此时慢指针的next是要被删除的node。
时间复杂度O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        slow, fast = dummyNode, dummyNode
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummyNode.next