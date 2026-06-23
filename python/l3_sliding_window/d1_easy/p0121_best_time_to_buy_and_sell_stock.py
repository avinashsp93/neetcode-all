class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        price_length = len(prices)

        if price_length == 1:
            return 0
        
        max_profit = 0

        while(right < price_length):
            if prices[left] > prices[right]:
                left+=1
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
            right+=1
        return max_profit