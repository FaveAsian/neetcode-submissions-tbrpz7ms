class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        res = 1
        for num in nums:
            if num not in count:
                count[num] = 0
            
            count[num] += 1
            if count[num] > n/2:
                res = num
                break
        return res
