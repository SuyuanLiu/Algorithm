'''
@lsy 2019.12.5

参考：https://leetcode.com/problems/max-points-on-a-line/discuss/221044/
有用到最大公约数的求法。
对每一个点，去计算其他点与它的斜率，然后存到哈希表中。
时间复杂度为O(n^2)
由于计算斜率涉及到浮点数精度问题，如果用乘法涉及到溢出问题，所以这边用公约数的方法去解决。
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        def frac(x, y):
            g = gcd(x, y)
            return x//g, y//g
        
        # code
        cnt = 0
        for i in range(len(points)):
            dic = {i: 1}
            same = 0
            for j in range(i+1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
            
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                elif dx == 0:
                    slope = i
                else:
                    slope = frac(dx, dy)
                
                if slope not in dic.keys():
                    dic[slope] = 1
                dic[slope] += 1
                
            cnt = max(cnt, max(dic.values())+same)
            
        return cnt
        
    
    