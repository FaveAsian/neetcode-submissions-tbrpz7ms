"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        top, bot = 0, n
        left, right = 0, n

        def dfs(top, bot, left, right):
            res = Node(False, 0, None, None, None, None)
            
            isLeaf, val = self.traverse(top, bot, left, right, grid)
            if isLeaf:
                res.val = val
                res.isLeaf = True
                return res

            # Divide into 4 section
            mid_row = top + ((bot-top)//2)
            mid_col = left + ((right-left)//2)
            # top left 0, 5, 0, 5
            res.topLeft = dfs(top, mid_row, left, mid_col)
            # top right 0, 5, 4, 8
            res.topRight = dfs(top, mid_row, mid_col, right)
            # bottom left 4, 8, 0, 5
            res.bottomLeft = dfs(mid_row, bot, left, mid_col)
            # bottom right 4, 8, 4, 8
            res.bottomRight = dfs(mid_row, bot, mid_col, right)

            return res

        return dfs(top, bot, left, right)
    

    # helper to traverse whole grid
    def traverse(self, top, bot, left, right, grid):
        val = grid[top][left]
        for i in range(top, bot):
            for j in range(left, right):
                if grid[i][j] != val:
                    return (False, -1)
        return (True, val)