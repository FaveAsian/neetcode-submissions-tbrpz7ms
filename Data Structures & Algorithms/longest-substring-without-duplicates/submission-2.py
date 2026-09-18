class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        i = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[r])
            res = max(res, r-i+1)

        return res