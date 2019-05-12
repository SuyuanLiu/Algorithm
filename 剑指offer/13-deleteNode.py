'''
解题思路：
直接把node的内容替换成node.next的内容即可。
注意的是：
- 如果node是尾结点，要进行判断
- 如果只有一个结点，并且要删除的是head，直接把head变为None
  (这里好像不用特别说明也可以，因为node，head指向同一个位置，改变一个就都变了)

时空复杂度：
- 时间复杂度 O(1)
- 空间复杂度 O(1)

Test Cases：
- node在链表中间
- node是头结点
- node是尾结点
- 链表只有一个元素，node是头结点

'''
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
