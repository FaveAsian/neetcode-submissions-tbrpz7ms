"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start = node.val
        graph = {}

        def dfs(curr):
            if not curr:
                return
            if curr in graph:
                return

            graph[curr] = Node(val=curr.val)

            neighbors_list = []
            for neigh in curr.neighbors:
                if neigh not in graph:
                    dfs(neigh)
                neighbors_list.append(graph[neigh])    
            graph[curr].neighbors = neighbors_list
                
        dfs(node)

        return graph[node]