class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        
        # Compute Prefix
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i-1])
        
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i+1])

        print(prefix, suffix)
        res = 0
        for i in range(n):
            water = min(prefix[i], suffix[i]) - height[i]
            print(water)
            res += max(0, water)

        return res
