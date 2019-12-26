'''
@lsy 2019.12.26 
拓扑排序（不是很明白）
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        from collections import deque
        
        adj = defaultdict(list)
        degree = [0] * numCourses
        
        for c, pre in prerequisites:
            adj[pre].append(c)
            degree[c] += 1
        
        queue = deque()
        for c in range(numCourses):
            if degree[c] == 0:
                queue.appendleft(c)
                
        while queue:
            cur = queue.pop()
            numCourses -= 1
            for nei in adj[cur]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.appendleft(nei)
                
        return numCourses == 0
            
        