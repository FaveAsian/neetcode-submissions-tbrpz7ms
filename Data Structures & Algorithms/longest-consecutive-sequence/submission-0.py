class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapping = {}
        res = 0

        for num in nums:
            mapping[num] = num + 1
        
        for key in mapping.keys():
            curr = 0
            tempKey = key
            while tempKey in mapping:
                curr += 1
                tempKey = mapping[tempKey]
            res = max(res, curr)

        return res