# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxi = float('-inf')
        def height(node):
            if not node:
                return 0
            left = max(0,height(node.left))
            right = max(0,height(node.right))
            currentPath = node.val + left + right
            self.maxi = max(self.maxi , currentPath)
            return node.val + max(left, right)
        height(root)
        return self.maxi