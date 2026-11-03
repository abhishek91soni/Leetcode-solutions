# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.previous = None
        self.reverse_preorder(root)
        return root
    def reverse_preorder(self, root):
        if root is None:
            return
        self.reverse_preorder(root.right)
        self.reverse_preorder(root.left)
        root.right = self.previous
        root.left = None
        self.previous = root
     