'''
@lsy  2019.9.25
二分法
每天运送的重量，一定在max(weights)和sum(weights)之间。
对这个重量区间二分，然后判断在当前重量下，能否在D天内完成运输。
如果当前重量符合要求，区间右端点移动到mid（注意不是-1，-1可能错过这个值）
如果当前重量不符合要求，区间左端点移动到mid+1.

要注意在isPosibleToShip里面，ship_day初值为1.

时间复杂度O(nlogn)
'''
class Solution:
    def isPosibleToShip(self, weights, D, ship_weight):
        ship_day, cur_weight = 1, 0 
        for w in weights:
            if cur_weight + w <= ship_weight:
                cur_weight += w
            else:
                cur_weight = w
                ship_day += 1
        return ship_day <= D
                
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if len(weights) == D:
            return max(weights)
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right-left)//2
            if self.isPosibleToShip(weights, D, mid):
                right = mid
            else:
                left = mid + 1
        return left
            
