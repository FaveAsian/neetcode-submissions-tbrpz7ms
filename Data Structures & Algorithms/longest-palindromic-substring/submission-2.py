class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        res = ""
        for i in range(len(s)):
            new_string = self.helper(i, s)
            
            if len(new_string) > len(res):
                res = new_string
        
        return res
    
    def helper(self, index, s):
        # consider both even and odd cases
        even = self.builder(index, index, s)
        odd = self.builder(index-1, index,s)

        if len(even) > len(odd):
            return even
        
        return odd
    
    def builder(self, l, r, s):
        new_str = ""

        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                new_str = s[l:r+1]
                l -= 1
                r += 1
            else:
                break
        return new_str
