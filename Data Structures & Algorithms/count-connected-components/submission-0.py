class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]
        res = 0

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def merge(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

        for n1, n2 in edges:
            merge(n1, n2)

        for i in range(n):
            if i == par[i]:
                res += 1

        return res

        