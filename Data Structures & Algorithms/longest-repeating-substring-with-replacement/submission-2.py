class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        most = 0
        res = 1
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1

            if most < count[s[r]]:
                most = count[s[r]]

            while (r-l+1)-most > k:
                count[s[l]] -= 1
                l += 1
            print(l, r)
            res = max(res, r-l+1)

        
        return res