class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitAcc = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                profitAcc += prices[i+1]-prices[i]
        return profitAcc
