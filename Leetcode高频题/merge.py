'''
@lsy 2019.11.14
对 intervals 排序，然后看下一个 interval 与上一个是否有重合之处。
Solution 2，更简洁一点。
'''
# Solution 1
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort()
        
        res, preInterval = [], []
        for n in intervals:
            if not preInterval:
                preInterval = n
                continue
            if n[0] <= preInterval[1]:
                preInterval[1] = max(preInterval[1], n[1])
            else:
                res.append(preInterval)
                preInterval = n

        res.append(preInterval)
            
        return res

# Solution 2
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        intervals.sort()
        
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
                
        return res
