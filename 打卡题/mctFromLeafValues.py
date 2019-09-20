'''
@lsy  2019.9.20
参考：https://blog.csdn.net/qq_17550379/article/details/97020009

DP，或者贪心，用单调栈。

DP：
dp[i,j]表示arr[i:j]的结果。
dp[i,j] = min(dp[i,j], dp[i,k-1]+dp[k,j]+max(arr[i:k])*max(arr[k:j+1]))

单调栈：
贪心策略：每次把两个最小的数字相乘，最后这些乘积加和是最小的。(不是很懂)
'''

# Solution 1: DP
class Solution:
    def __init__(self):
        self.dp = {}
    
    def helper(self, i, j, arr):
        if i >= j:
            return 0
        if (i,j) in self.dp:
            return self.dp[(i,j)]
        
        res = float('inf')
        for k in range(i+1, j+1):
            res = min(res, self.helper(i,k-1,arr) + self.helper(k,j,arr) + max(arr[i:k])*max(arr[k:j+1]))
        self.dp[(i,j)] = res
        return res
        
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.helper(0, len(arr)-1, arr)
        
        

# Solution 2： stack
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]
        for n in arr:
            while n >= stack[-1]:
                tmp = stack.pop()
                res += tmp * min(n, stack[-1])
            stack.append(n)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
            
        return res
