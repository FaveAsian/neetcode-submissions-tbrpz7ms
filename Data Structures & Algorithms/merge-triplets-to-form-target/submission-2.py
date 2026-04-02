class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        track = [0, 0, 0]
        a, b, c = target[0], target[1], target[2]
        for i, j, k in triplets:
            if i <= a and j <= b and k <= c:
                track[0] = max(track[0], i)
                track[1] = max(track[1], j)
                track[2] = max(track[2], k)
            if track == target:
                return True

        return False


        