'''
@lsy 2019.10.31

归并排序。
利用merge two lists方法。

TODO：
使用优先队列方法。见Discuss
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummyNode = ListNode(0)
        node = dummyNode
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return dummyNode.next        
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) < 2:
            return None if not lists else lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)
        
        