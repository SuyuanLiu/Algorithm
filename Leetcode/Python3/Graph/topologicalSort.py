'''
Solution:
- 使用BFS，时间复杂度 O(n), 空间复杂度 O(n)。
- 有向图有入度和出度的概念。拓扑排序的话，第一个结点肯定是入度为0的点。因此进行排序，可以从入度为0的点开始，然后删掉这个点（以及这个点对应的边），然后寻找下一个入度为0的点，直到最后。
- 最开始先扫一遍图，记录以下每个点的入度是多少，然后找到入度为0的点，放到队列中，以用来后续的遍历。
- 这边要注意的是，在最开始的时候可能会有多个入度为0的node。
'''
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return 
        
        res = []
        dic = {node: 0 for node in graph}
        
        for node in graph:
            for nei in node.neighbors:
                if nei in dic:
                    dic[nei] += 1 
            
        queue = [node for node in dic if dic[node] == 0]
        
        while queue:
            node = queue.pop(0)
            res.append(node)
            for nei in node.neighbors:
                dic[nei] -= 1 
                if dic[nei] == 0:
                    queue.append(nei)
        
        return res
