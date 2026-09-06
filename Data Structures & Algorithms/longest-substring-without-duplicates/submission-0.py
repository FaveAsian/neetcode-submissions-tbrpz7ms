class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        seen.add(s[0])
        i, j = 0, 1
        res = 1
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            j += 1
            res = max(res, j-i)

        return res