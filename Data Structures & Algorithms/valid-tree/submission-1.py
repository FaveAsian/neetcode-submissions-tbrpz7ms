class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection
        graph = {i: [] for i in range(n)}

        # make it directed so it can only flow one way for easier cycle detection
        for origin, dst in edges:
            graph[origin].append(dst)
            graph[dst].append(origin)

        visited = set()

        def dfs(node, parent) -> bool:
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False

            return True 
        
        return dfs(0, -1) and len(visited) == n 