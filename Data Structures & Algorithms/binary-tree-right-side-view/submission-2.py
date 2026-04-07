# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        
        # use BFS to go level by level, append the last one to res
        while queue:
            n = len(queue)
            last_seen = None
            for i in range(n):
                node = queue.popleft()
                if node:
                    last_seen = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            
            if last_seen:
                res.append(last_seen)


        return res
                