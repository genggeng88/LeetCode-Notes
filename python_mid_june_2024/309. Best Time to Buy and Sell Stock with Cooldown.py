class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            old_held = held
            held = max(held, reset - price)
            reset = max(reset, sold)
            sold = old_held + price

        return max(reset, sold)