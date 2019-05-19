'''
解题思路：
分为两个步骤：复制结点，复制连接。
- 如果在复制结点的时候，把next一起复制，但是random的复制只能在下一步进行复制，每次复制都要从头找到这个结点，太耗时。
- 使用哈希表，在复制结点的时候，把node与对应复制的结点作为一对键值对放到字典里面；然后在遍历原链表，把对应关系复制即可。

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)

Test Cases：
- 空链表
- random指向自己等；只有一个元素

'''
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        Head = RandomListNode(pHead.label)
        dic = {None: None}

        # clone nodes
        cur = pHead
        while cur:
            node = RandomListNode(cur.label)
            dic[cur] = node
            cur = cur.next
        
        # clone relationships
        cur = pHead
        while cur:
            dic[cur].next = dic[cur.next]
            dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[pHead]
