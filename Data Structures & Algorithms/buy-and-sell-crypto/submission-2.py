class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i, p in enumerate(prices):
            min_price = min(p, min_price)
            max_profit = max(max_profit, p - min_price) 
        
        return max_profit


            
        # [10,1,5,6,7,1]