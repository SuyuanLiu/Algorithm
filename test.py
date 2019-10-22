class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or abs(x) > 0x7fffffff:
            return 0
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x != 0:
            tmp = x % 10
            res = res * 10 + tmp
            x = int(x / 10)
        return res * sign
            
        
        
s = Solution()
print(s.reverse(-124))