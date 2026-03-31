class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [0] * (n*2)

        for i, _ in enumerate(results):
            results[i] = nums[i%n]
        
        return results