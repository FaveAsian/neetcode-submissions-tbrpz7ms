class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(curr, used):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            for i in range(n):
                if used[i]:
                    continue

                curr.append(nums[i])
                used[i] = True
                dfs(curr, used)

                curr.pop()
                used[i] = False

            
        tracking = [False for _ in range(n)] 
        dfs([], tracking)
        return res