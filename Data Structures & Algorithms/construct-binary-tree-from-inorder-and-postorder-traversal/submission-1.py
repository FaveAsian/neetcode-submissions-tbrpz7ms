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

        def dfs(inorder, postorder):
            if not inorder or not postorder:
                return None

            root = postorder[-1]
            pivot_in = inorder.index(root)
            left_inorder = inorder[0:pivot_in]
            right_inorder = inorder[pivot_in+1:]
            left_postorder = postorder[:pivot_in]
            right_postorder = postorder[pivot_in:-1]
            node = TreeNode(val=root)
            node.left = dfs(left_inorder, left_postorder)
            node.right = dfs(right_inorder, right_postorder)

            return node


        return dfs(inorder, postorder)
