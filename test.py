
class listNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def deleteNode(self, head, node):
        if not head:
            return 

        if not node.next:
            pre, cur = None, head
            while cur != node:
                pre = cur
                cur = cur.next
            pre.next = None
            return
        
        if node == head and not node.next:
            head = None

        tmp = node.next
        node.val = tmp.val
        node.next = tmp.next

head = listNode(1)
head.next = listNode(2)
head.next.next = listNode(3)
print(head.val)
print(head.next.val)
print(head.next.next.val)

s = Solution()
s.deleteNode(head, head.next.next)
print(head.val)
print(head.next.val)
print(head.next.next.val)
