class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {str(i+1): chr(ord("A") + i) for i in range(26)}
        cache = {}
        n = len(s)
        # use backtracking
        def dfs(index):
            if index == n:
                return 1
            if index > n:
                return 0
            if s[index] == "0":
                return 0
            if index in cache:
                return cache[index]
            
            double_digit = 0
            if 10 <= int(s[index:index+2]) <= 26:
                double_digit = dfs(index+2)

            cache[index] = dfs(index+1) + double_digit
            
            return cache[index]
        
        return dfs(0) 