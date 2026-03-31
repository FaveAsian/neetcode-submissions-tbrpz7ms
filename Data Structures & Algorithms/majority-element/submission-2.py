class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_count = 0
        res = 1
        for num in nums:
            if num not in count:
                count[num] = 0
            
            count[num] += 1
            if count[num] > max_count:
                res = num
                max_count = count[num]
        return res
