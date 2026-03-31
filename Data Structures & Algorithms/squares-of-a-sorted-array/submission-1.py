class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        l, r = 0, len(nums)-1
        idx = len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[idx] = nums[l] * nums[l]
                l += 1
            else:
                res[idx] = nums[r] * nums[r]
                r -= 1
            idx -= 1
            
        return res