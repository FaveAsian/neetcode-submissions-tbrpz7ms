class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        res = 0
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            target = current_sum - k

            if target in seen:
                res += seen[target]
            
            if current_sum not in seen:
                seen[current_sum] = 0
            seen[current_sum] += 1

        return res