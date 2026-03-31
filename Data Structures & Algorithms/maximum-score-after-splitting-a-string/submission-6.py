class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0] * len(s)
        suffix = [0] * len(s)
        prefix[0] = 1 if s[0] == "0" else 0
        suffix[-1] = 1 if s[-1] == "1" else 0

        for i in range(1, len(s)-1):
            prefix[i] = prefix[i-1]
            if s[i] == "0":
                prefix[i] += 1
        
        for i in range(len(s)-2, 0, -1):
            suffix[i] = suffix[i+1]
            if s[i] == "1":
                suffix[i] += 1

        res = 1
        for i in range(len(s)):
            res = max(res, prefix[i-1] + suffix[i])

        return res

# 011101
# [1, 1, 1, 1, 2, 0]
# [0, 4, 3, 2, 1, 1]
# [1, 5, 4, 3, 3, 1]