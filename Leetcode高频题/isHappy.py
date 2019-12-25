'''
@lsy 2019.12.25

Solution 1:
弗洛伊德圆环。类似链表是否有环。使用快慢指针。
- 两个数，A，B；
- 从A出发，经过如题操作，一定会最终到达B数
- 从B出发，经过如题操作，一定会再次回到B数

Solution 2：哈希表（TODO）
'''
# Solution 1
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(fast)
            if fast == 1:
                return True
            fast = self.squareSum(fast)
            if fast == 1:
                return True
            
            if slow == fast:
                break
        return slow == 1
        
    def squareSum(self, n):
        res = 0
        while n:
            tmp = n % 10
            res += tmp ** 2
            n //= 10
        return res