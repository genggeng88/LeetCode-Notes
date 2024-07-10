class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        leftProfit = [0] * n
        rightProfit = [0] * (n+1)

        buy_at = prices[0]
        sell_at = prices[n-1]

        for i in range(1, n):
            leftProfit[i] = max(leftProfit[i-1], prices[i]-buy_at)
            buy_at = min(buy_at, prices[i])
            
            r = n-1-i
            rightProfit[r] = max(rightProfit[r+1], sell_at-prices[r])
            sell_at = max(sell_at, prices[r])
            
        res = 0
        for i in range(n):
            res = max(res, leftProfit[i]+rightProfit[i+1])
        
        return res