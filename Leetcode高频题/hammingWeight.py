'''
@lsy 2019.12.24

Solution 1:
用 n & 1 判断最后一位是否为 1，然后对 n 右移。

Solution 2：
n &= n - 1，不是很懂
'''
# Solution 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        
        for _ in range(32):
            if n & 1 == 1:
                cnt += 1
            n >>= 1
            
        return cnt
    
# Solution 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        
        while n:
            n &= n - 1
            cnt += 1
            
        return cnt