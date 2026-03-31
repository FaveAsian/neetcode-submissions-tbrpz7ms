class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        first = [0] * (len(nums)-1)
        first[0] = nums[0]
        first[1] = max(nums[0], nums[1])
        
        # situation where we take from first house
        for i in range(2, len(nums)-1):
            first[i] = max(first[i-1], nums[i] + first[i-2])

        second = [0] * len(nums)
        second[1] = nums[1]
        second[2] = max(nums[1], nums[2])

        # situation where we take from second house first
        for i in range(3, len(nums)):
            second[i] = max(second[i-1], nums[i] + second[i-2])
        
        return max(first[-1], second[-1])
