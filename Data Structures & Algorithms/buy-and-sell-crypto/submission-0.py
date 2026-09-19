class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > curr:
                res = max(res, prices[i]-curr)
            else:
                curr = prices[i]
        return res