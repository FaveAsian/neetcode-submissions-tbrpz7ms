class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = nums[0]

        for num in nums:
            tmp = curMax * num
            curMax = max(num*curMax, num*curMin, num)
            curMin = min(tmp, num*curMin, num)
            res = max(res, curMax)
        
        return res