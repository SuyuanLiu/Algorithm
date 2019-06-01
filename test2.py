
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def lengthOfLinkedList(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l 
    
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        
        l1, l2 = self.lengthOfLinkedList(pHead1), self.lengthOfLinkedList(pHead2)
        node1, node2 = pHead1, pHead2
        if l1 < l2:
            l1, l2 = l2, l1
            node1, node2 = node2, node1
            
        for i in range(l1 - l2):
            nod1 = node1.next
        while node1 != node2:
            node1, node2 = node1.next, node2.next
        return node1
        

s = Solution()
h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(3)
h2 = ListNode(6)
h2.next = h1.next
print(s.FindFirstCommonNode(h1, h2).val)
