'''
@lsy 2019.11.25

DP.
dp[i]表示在第i天，卖出。dp[i] = max(prices[i] - min_price, 0)
进一步简化，只要一个变量记录最低的价格min_price，一个变量记录最高利润max_profit.
时间复杂度O(n)，空间复杂度O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        min_price, max_profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] >= min_price:
                max_profit = max(max_profit, prices[i]-min_price)
            else:
                min_price = prices[i]
        return max_profit