class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count # n
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # sort them into buckets
        freq = [[] for _ in range(len(nums)+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, -1, -1):
            while freq[i] != []:
                res.append(freq[i].pop())
                if len(res) == k:
                    return res
        # return 
        # return res