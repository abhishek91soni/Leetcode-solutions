# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        sumleft = 0
        def suml(node):
            nonlocal sumleft
            if node is None :
                return 0
            if node.left:
                if node.left.right is None and node.left.left is None:
                    sumleft = sumleft + node.left.val
            suml(node.left)
            suml(node.right)
        suml(root)
        return sumleft 