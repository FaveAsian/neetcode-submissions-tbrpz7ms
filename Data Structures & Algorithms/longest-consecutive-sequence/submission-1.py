class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            if (num-1) not in numSet:
                curr = 1
                while (num + curr) in numSet:
                    curr += 1
                res = max(curr, res)

        return res