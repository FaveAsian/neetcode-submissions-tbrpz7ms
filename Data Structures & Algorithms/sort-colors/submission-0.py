class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort
        count = {i: 0 for i in range(3)}
        for num in nums:
            count[num] += 1

        idx = 0
        for color, freq in count.items():
            for _ in range(freq):
                nums[idx] = color
                idx += 1
        