'''
Solution:
- 对intervals按元素的start进行排序，然后遍历一遍，把重叠的部分合并起来即可。
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals = sorted(intervals, key=lambda s: s.start)
        res = []
        
        for it in intervals:
            if not res:
                res.append(it)
            else:
                if res[-1].start <= it.start <= res[-1].end:
                    res[-1].end = max(res[-1].end, it.end)
                else:
                    res.append(it)
        return res
