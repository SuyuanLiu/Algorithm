class Solution():
    def deleteNode(self, head, node):
        if not head:
            return 

        if not node.next:
            node = None
            return 
        
        if node == head and not node.next:
            head = None

        tmp = node.next
        node.val = tmp.val
        node.next = tmp.next
