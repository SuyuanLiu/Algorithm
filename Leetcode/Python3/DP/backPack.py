'''
Solution:
- 0-1背包
- 定义dp，dp[i][j]表示前i件商品能否组成j的背包，能的话就是True，否则是False；
- 动态方程：dp[i][j] = dp[i-1][j]， if A[i-1] > j
                     dp[i-1][j-A[i-1]] or dp[i-1][j]
- 初始化：dp[0][0] = True，dp[i][0] = True，前i件商品构成0的背包，一个都不取就可以了；
- 结果：最后一行，即前i个商品能构成的背包的大小，从m向前遍历，第一个为True的就是最终结果；

More
- https://www.jiuzhang.com/solution/backpack/#tag-highlight-lang-python有更多的解法

'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if not A or m < 1:
            return 0
            
        dp = [[False for j in range(m+1)] for i in range(len(A)+1)]
        dp[0][0] = True
                
        for i in range(1, len(A)+1):
            dp[i][0] = True
            for j in range(1, m+1):
                if A[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-A[i-1]] or dp[i-1][j]
                    
        for j in range(m, -1, -1):
            if dp[-1][j]:
                return j
        return 0
