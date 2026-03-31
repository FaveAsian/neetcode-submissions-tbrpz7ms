class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ret = False
        seen = []
        for num in nums:
            if num in seen:
                ret = True
                break
            else:
                seen.append(num)
        return ret