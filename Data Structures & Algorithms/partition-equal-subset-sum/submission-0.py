class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        half = sum(nums)//2
        cache = {}

        return self.helper(half, nums, 0, 0, cache)


    def helper(self, half, nums, i, total, cache):
        if total == half:
            return True
        if total > half or i >= len(nums):
            return False
        if (i, total) in cache:
            return cache[(i, total)]
        
        # Skip
        first = self.helper(half, nums, i+1, total, cache)
        
        # Pick current one
        second = self.helper(half, nums, i+1, total+nums[i], cache)
        cache[(i, total)] = first or second
        return cache[(i, total)]