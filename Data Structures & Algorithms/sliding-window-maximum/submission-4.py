class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        queue = deque()
        for i, val in enumerate(nums):
            # 1. Evict elements outside current window
            if queue and queue[0] <= i - k:
                queue.popleft()
            # 2. Maintain monotonic decreasing order
            while queue and nums[queue[-1]] < val:
                queue.pop()
            queue.append(i)
            # 3. Window is fully formed
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res