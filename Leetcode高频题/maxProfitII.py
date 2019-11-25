'''
@lsy 2019.11.25
贪心算法。
buyin_price为买入价格，如果当前价格高于买入，立即卖出；
否则以当前价格作为买入价格。
时间复杂度O(n)，空间复杂度O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        buyin_price, max_profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] > buyin_price:
                max_profit += prices[i] - buyin_price
            buyin_price = prices[i]
        
        return max_profit