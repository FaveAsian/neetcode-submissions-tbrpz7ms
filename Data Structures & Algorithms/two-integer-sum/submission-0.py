class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i, num in enumerate(nums):
            val = target - num
            if val in diff:
                return [diff[val], i]
            diff[num] = i