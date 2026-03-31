# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        res = -1
        cnt = 0
        def get_k(node):
            nonlocal res
            nonlocal cnt
            if not node:
                return None
            get_k(node.left)
            cnt += 1
            if cnt == k:
                res = node.val

            get_k(node.right)

        get_k(root)
        return res