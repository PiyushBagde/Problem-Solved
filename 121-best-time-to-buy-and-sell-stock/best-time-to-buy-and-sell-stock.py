class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minn = prices[0]

        for i in range(1,len(prices)):
            cost = prices[i] - minn
            profit = max(profit, cost)
            minn = min(prices[i], minn)
        return profit

        