class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = float("inf")

        for price in prices:
            curr = min(curr, price)
            res = max(res, price-curr)
        return res