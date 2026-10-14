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
        arr = []
        if root is None:
            return 
        def preorder(node):
            if node is None:
                return
            arr.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        for i in range(len(arr)-1):
            arr[i].left = None
            arr[i].right = arr[i+1]
        arr[-1].left = None
        arr[-1].right = None