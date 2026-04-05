class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # just keep adding, reset to 0 if we go negative
        cur = 0
        res = float("-inf")

        for num in nums:
            cur += num
            res = max(res, cur)

            if cur < 0:
                cur = 0
        
        return res