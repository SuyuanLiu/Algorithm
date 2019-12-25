'''
@lsy 2019.12.25

不是很懂
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        strikes = [1] * n
        strikes[0], strikes[1] = 0, 0
        
        import math
        for i in range(2, int(math.sqrt(n))+1):
            if strikes[i] != 0:
                strikes[i*i : n : i] = [0] * ((n-1-i*i)//i + 1)
                
        return sum(strikes)