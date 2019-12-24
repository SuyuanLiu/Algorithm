'''
@lsy 2019.12.24

用 n & 1 取出数字 n 的最后一位加入 res；
然后 n 右移一位，res 左移；
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for _ in range(32):
            # res = (res << 1) + (n & 1)
            res = (res << 1) | (n & 1)
            n >>= 1
            
        return res