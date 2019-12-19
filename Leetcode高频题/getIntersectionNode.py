'''
@lsy 2019.12.19

Solution 1:
使用两个栈，分别将两个链表装入栈中，然后从最后一个节点开始比较，找出相交点。

Solution 2：
将A链表放入set中，遍历链表B，如果当前节点在set中，说明当前节点就是相交点。
注意使用set，若使用列表，会超时。
'''
# Solution 1
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        sA, sB = [], []
        while headA:
            sA.append(headA)
            headA = headA.next
            
        while headB:
            sB.append(headB)
            headB = headB.next
            
        pre = None
        while sA and sB:
            nodeA, nodeB = sA.pop(), sB.pop()
            if nodeA != nodeB:
                return pre
            pre = nodeA
            
        return pre


# Solution 2
# class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next
            
        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
            
        return None
            