# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append((root, 0)) #TreeNode, col
        mapping = defaultdict(list)
        res = []
        min_col = 0
        max_col = 0

        while queue:
            que_len = len(queue)
            for _ in range(que_len):
                node, col = queue.popleft()
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                mapping[col].append(node.val)

                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
                
        for key in range(min_col, max_col+1):
            res.append(mapping[key])
        
        return res
