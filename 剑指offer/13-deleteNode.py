'''
解题思路：
直接把node的内容替换成node.next的内容即可。
注意的是：
- 如果node是尾结点，要从头遍历，把倒数第二个结点的next指向None，不能直接把node变为None，因为倒数第二个结点还是指向了之前的Node结点。
- 如果只有一个结点，并且要删除的是head，直接把head变为None
  (这里好像不用特别说明也可以，因为node，head指向同一个位置，改变一个就都变了)
- 删除尾结点时间复杂度是O(n)，对于长度为n的链表，前n-1个结点的时间复杂度是O(1)
  所以平均时间复杂度是 [ O(1) * (n-1) + O(n) ] / n = O(1)

时空复杂度：
- 时间复杂度 O(1)
- 空间复杂度 O(1)

Test Cases：
- node在链表中间
- node是头结点
- node是尾结点
- 链表只有一个元素，node是头结点

⚠️
要询问面试官，待删除结点是否一定在链表内，如果不一定在的话，时间复杂度就无法达到O(1).
'''
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
