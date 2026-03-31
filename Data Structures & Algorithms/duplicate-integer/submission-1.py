class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ret = False
        seen = set()
        for num in nums:
            if num in seen:
                ret = True
                break
            else:
                seen.add(num)
        return ret