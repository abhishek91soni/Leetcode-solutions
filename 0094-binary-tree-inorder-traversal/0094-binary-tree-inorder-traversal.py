# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        arr = []
        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            arr.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return arr
