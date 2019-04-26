'''
Solution:
- 克隆图，分为两个部分：克隆图中的点，克隆边
- 克隆点，使用BFS遍历。维护一个队列，把node的neighbors放到队列中去。（图的遍历推荐使用BFS）
- 注意：在克隆点的时候，用一个map把克隆的点与之前的点联系起来，否则找不到对应的联系

Solution 1:
克隆点和克隆边分为两个步骤。因为两个步骤都是BFS的顺序，把之前的点放到一个list里面存一下，克隆边的时候直接读取即可。（看起来更清晰）
Solution 2:
在克隆点的过程中，一起克隆了边。

时间复杂度: O(n)
空间复杂度: O(n)
'''
# Solution 2
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        queue = [node]
        dic = {node: Node(node.val, [])}
        
        while queue:
            tmpNode = queue.pop(0)
            tmpNewNode = dic[tmpNode]
            for neibor in tmpNode.neighbors:
                if neibor in dic:
                    tmpNewNode.neighbors.append(dic[neibor])
                    continue
                queue.append(neibor)
                dic[neibor] = Node(neibor.val, [])
                tmpNewNode.neighbors.append(dic[neibor])
                
        return dic[node]

# Solution 1
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        queue = [node]
        nodes = [node]
        dic = {node: Node(node.val, [])}
        
        while queue:
            tmpNode = queue.pop(0)
            for neibor in tmpNode.neighbors:
                if neibor in dic:
                    continue
                queue.append(neibor)
                nodes.append(neibor)
                dic[neibor] = Node(neibor.val, [])
                
        for tmpNode in nodes:
            tmpNewNode = dic[tmpNode]
            for nei in tmpNode.neighbors:
                tmpNewNode.neighbors.append(dic[nei])
        
        return dic[node]
