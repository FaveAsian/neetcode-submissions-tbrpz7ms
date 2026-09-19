class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_index = {}
        count = [0] * 26

        for i in range(len(s)):
            char = s[i]
            count_idx = ord(char) - ord("a")

            if count_idx not in first_index:
                first_index[count_idx] = i
            count[count_idx] += 1
        
        res = float("inf")
        for i in range(26):
            if count[i] == 0 or count[i] > 1:
                continue
            res = min(res, first_index[i])

        return -1 if res==float("inf") else res
            
