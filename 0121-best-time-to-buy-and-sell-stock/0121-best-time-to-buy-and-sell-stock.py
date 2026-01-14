class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxProfit = 0

        for price in prices:
            profit = price - low

            low = min(price, low)
            maxProfit = max(profit, maxProfit)

        return maxProfit