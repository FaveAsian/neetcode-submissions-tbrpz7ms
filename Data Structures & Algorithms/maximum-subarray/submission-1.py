class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # just keep adding, reset to 0 if we go negative
        cur = 0
        res = float("-inf")

        for num in nums:
            cur = max(num, cur+num)
            res = max(res, cur)
        
        return res