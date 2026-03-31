class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]

        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        res = [1] * len(nums)
        
        # go through pre
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        coef = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= coef
            coef *= nums[i]

        return res