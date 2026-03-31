# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # [2, 1, 3, 4]
        # [2, 4, 3, 1]
        
        # the last one in post order is the root
        # In in order, the left side, is the left tree and right is right tree

        inorderIdx = {v: i for i, v in enumerate(inorder)}

        def dfs(l, r):
            if l > r:
                return None

            root = postorder.pop()
            pivot_in = inorderIdx[root]
            node = TreeNode(val=root)
            node.right = dfs(pivot_in+1, r)
            node.left = dfs(l, pivot_in-1)

            return node


        return dfs(0, len(inorder)-1)
