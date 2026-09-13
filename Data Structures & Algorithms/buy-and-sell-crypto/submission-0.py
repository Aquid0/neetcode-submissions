class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0] 
        mx = 0

        for i in range(len(prices)):
            mx = max(mx, prices[i] - mi)
            mi = min(mi, prices[i])

        return mx