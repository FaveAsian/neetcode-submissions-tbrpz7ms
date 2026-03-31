class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # so there are 0->(n-1) nodes
        # Use dfs to explore each root
        # keep dictionary of height -> list[roots]
        
        def bfs(node: int) -> int:
            queue = deque()
            queue.append(node)

            level = 0
            while queue:
                neigbors_len = len(queue)
                for _ in range(neigbors_len):
                    neighbor = queue.popleft()
                    visited.add(neighbor)
                    for neigh in graph[neighbor]:
                        if neigh in visited:
                            continue
                        queue.append(neigh)
                level += 1
            return level         

        # create graph
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        mhts = defaultdict(list)

        visited = set()
        for i in range(n):
            visited.clear()
            mht = bfs(i)
            mhts[mht].append(i)
        
        lowest = min(mhts.keys())
        return mhts[lowest]