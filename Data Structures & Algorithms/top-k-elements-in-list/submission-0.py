class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count # n
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # heapify # n
        heap = [(cnt, num) for num, cnt in count.items()]
        heapq.heapify_max(heap)
        # pop # klogk
        res = []
        for _ in range(k):
            # print(heap)
            _, num = heapq.heappop_max(heap)
            res.append(num)

        # return 
        return res