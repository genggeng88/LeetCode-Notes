class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_at = prices[0]

        for price in prices:
            if price < buy_at:
                buy_at = price
            else:
                max_profit += price - buy_at
                buy_at = price
        return max_profit